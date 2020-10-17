from schema_registry.client import SchemaRegistryClient, schema
from schema_registry.serializers import FaustSerializer

from simple_settings import settings

from example.users.models import AdvanceUserModel

# Initialize Schema Registry Client
client = SchemaRegistryClient(url=settings.SCHEMA_REGISTRY_URL)

avro_user_schema = schema.AvroSchema({
     "type": "record",
     "namespace": "com.example",
     "name": "AvroUsers",
     "fields": [
       {"name": "first_name", "type": "string"},
       {"name": "last_name", "type": "string"}
     ]
})

avro_user_serializer = FaustSerializer(client, "users", avro_user_schema)

# example of how to use it with dataclasses-avroschema
avro_advance_user_serializer = FaustSerializer(
    client, "advance_users", AdvanceUserModel.avro_schema())


def avro_user_codec():
    return avro_user_serializer


def avro_advance_user_codec():
    return avro_advance_user_serializer
