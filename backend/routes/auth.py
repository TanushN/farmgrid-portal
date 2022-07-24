import os

from fastapi import HTTPException, Depends, APIRouter
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from passlib.context import CryptContext
import sys

sys.path.insert(0, "../")

from backend.modules.users_db import UserDB

router = APIRouter(
    prefix="/auth",
)

# unique_id = str(uuid4())
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class NewUser(BaseModel):
    email: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET")
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = False
    authjwt_cookie_csrf_protect: bool = True
    authjwt_cookie_samesite: str = 'none'


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/signup')
def signup(user: NewUser):
    if user.email == "" and user.password == "":
        raise HTTPException(status_code=400, detail="fields cannot be empty")

    user_db = UserDB()
    if user_db.email_exists(user.email):
        raise HTTPException(status_code=409, detail="Email already exists")

    user_db = UserDB().insert(user.email, get_password_hash(user.password))

    return {"message": "successfully created user."}


@router.post('/login')
def login(user: NewUser, Authorize: AuthJWT = Depends()):
    if user.email == "" and user.password == "":
        raise HTTPException(status_code=400, detail="fields cannot be empty")

    user_record = UserDB().get_user(user.email)

    if not user_record:
        raise HTTPException(status_code=400, detail="Email and password do not match.")

    if not verify_password(user.password, user_record["hashed_password"]):
        raise HTTPException(status_code=400, detail="Email and password do not match.")

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)

    return {"email": user_record['email']}


@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@router.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}


@router.get("/getUsers")
def get_users():
    users = UserDB().get_table("users")
    response = users.scan(FilterExpression=Attr('email').eq('test@email.com'))
    data = response['Items']

    print(data)

    return {"hello": "world"}
