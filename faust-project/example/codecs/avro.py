from avro.schema import SchemaFromJSONData

from schema_registry.client import SchemaRegistryClient

from simple_settings import settings

from .serializers import AvroSerializer


# Initialize Schema Registry Client
client = SchemaRegistryClient(url=settings.SCHEMA_REGISTRY_URL)

avro_user_schema = SchemaFromJSONData({
     "type": "record",
     "namespace": "com.example",
     "name": "AvroUsers",
     "fields": [
       {"name": "first_name", "type": "string"},
       {"name": "last_name", "type": "string"}
     ]
})

avro_user_serializer = AvroSerializer(
  schema_registry_client=client,
  destination_topic="users",
  schema=avro_user_schema
)


def avro_user_codec():
    return avro_user_serializer
