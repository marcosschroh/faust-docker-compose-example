import faust

from dataclasses_avroschema import AvroModel


class UserModel(faust.Record, serializer='avro_users'):
    first_name: str
    last_name: str


class AdvanceUserModel(faust.Record, AvroModel, serializer='avro_advance_users'):
    first_name: str
    last_name: str
    age: int
