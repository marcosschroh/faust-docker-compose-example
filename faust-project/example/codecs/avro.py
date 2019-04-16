from avro.schema import SchemaFromJSONData

from example.helpers.avro.schema_registry.client import CachedSchemaRegistryClient
from example.helpers.avro.serializer.faust_avro_serializer import AvroSerializer

from simple_settings import settings


SCHEMA_REGISTRY_URL = settings.SCHEMA_REGISTRY_URL

# Initialize Schema Registry Client
client = CachedSchemaRegistryClient(url=SCHEMA_REGISTRY_URL)

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
        schema=avro_user_schema)


def avro_user_codec():
    return avro_user_serializer
