import boto3
from boto3.dynamodb.conditions import Attr
from boto3_type_annotations.dynamodb import ServiceResource
import hashlib


def get_id(email):
    return hashlib.sha256(str.encode(email)).hexdigest()


class UserDB:

    def __init__(self):
        self.db: ServiceResource = boto3.resource("dynamodb")
        self.db = self.db.Table("users")

    def email_exists(self, email):
        resp = self.db.scan(FilterExpression=Attr("email").eq(email))

        return True if resp["Items"] else False

    def insert(self, email, hashed_password):
        self.db.put_item(Item={'id': get_id(email), 'email': email, 'hashed_password': hashed_password})

    def get_user(self, email):
        resp = self.db.get_item(Key={'id': get_id(email)})
        if "Item" not in resp:
            return None
        else:
            return resp["Item"]

