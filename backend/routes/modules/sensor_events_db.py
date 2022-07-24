import boto3
from boto3.dynamodb.conditions import Key, Attr
from boto3_type_annotations.dynamodb import ServiceResource
import hashlib


class SensorEventsDB:

    def __init__(self):
        self.db: ServiceResource = boto3.resource("dynamodb")
        self.db = self.db.Table("sensor_events")

    def get_events(self, sensor_id):
        resp = self.db.query(KeyConditionExpression=Key("id").eq(sensor_id), ScanIndexForward=False)

        if "Items" not in resp:
            return None
        else:
            return resp["Items"]

