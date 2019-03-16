import logging
import logging.config
import os

import faust
from faust.serializers import codecs

from example import SETTINGS
from example.utils.avro.cached_schema_registry_client import CachedSchemaRegistryClient
from example.utils.avro.serializer.faust_avro_serializer import FaustAvroSerializer
from example.utils.config_base import load_config

logger = logging.getLogger(__name__)

# CONFIG = load_config(os.environ.get('CONFIG'))()

KAFKA_BROKER = SETTINGS.get("confluent", "bootstrap.servers")
SCHEMA_REGISTRY_URL = SETTINGS.get("confluent", "schema.registry.url")

app = faust.App(
    version=1,
    autodiscover=True,
    origin='example',
    id="1",
    broker=KAFKA_BROKER,
)


def main() -> None:
    app.main()
# source_topic = app.topic(CONFIG.source_topic, value_serializer="FaustAvroSerializer")

# out_topic = app.topic(
#     CONFIG.output_topic,
#     value_serializer="FaustAvroSerializer",
#     key_serializer="FaustAvroKeySerializer")

# schema_registry_client = CachedSchemaRegistryClient(url=SCHEMA_REGISTRY_URL)
# out_schema = parse_schema_descriptor(CONFIG.output_value_schema)
# out_key_schema = parse_schema_descriptor(CONFIG.output_key_schema)

# codecs.register(
#     "FaustAvroSerializer", 
#     FaustAvroSerializer(
#         schema_registry_client=schema_registry_client,
#         destination_topic=out_topic.topics[0],
#         schema=out_schema.schema))

# codecs.register(
#     "FaustAvroKeySerializer",
#     FaustAvroSerializer(
#         schema_registry_client=schema_registry_client,
#         destination_topic=out_topic.topics[0],
#         schema=out_key_schema.schema,
#         is_key=True))


# @app.agent(source_topic)
# async def score(stream):
#     async for records in stream.take(1000, within=30):
#         # Your processing code here
#         logger.info("Your code goes here...")
