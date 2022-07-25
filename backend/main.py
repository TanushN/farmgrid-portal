import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, sensor_events
import boto3

origins = [
    "http://localhost:3000",
    "https://farmgrid-portal.vercel.app",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(sensor_events.router)

boto3.setup_default_session(region_name=os.getenv("REGION_NAME"))

@app.get("/hello")
def hi():
    return {"hello": "world"}


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
