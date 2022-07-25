from fastapi import HTTPException, Depends, APIRouter
from fastapi_jwt_auth import AuthJWT

from .modules.sensor_events_db import SensorEventsDB

router = APIRouter(
    prefix="/sensor_events",
)


@router.get("/{sensor_id}")
def get_sensor_events(sensor_id: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    db = SensorEventsDB()
    resp = db.get_events(sensor_id)

    if not resp:
        return HTTPException(status_code=400, detail="Data cannot be fetched for this sensor.")

    return resp
