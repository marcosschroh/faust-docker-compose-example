import faust


class UserModel(faust.Record, serializer='avro_users'):
    first_name: str
    last_name: str
