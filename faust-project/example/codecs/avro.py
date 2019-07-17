from schema_registry.client import SchemaRegistryClient, schema
from schema_registry.serializers import FaustSerializer

from simple_settings import settings


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


def avro_user_codec():
    return avro_user_serializer
