from faust.serializers.codecs import Codec

from schema_registry.serializer import MessageSerializer

from typing import Dict


class AvroSerializer(MessageSerializer, Codec):

    def __init__(self, schema_registry_client, destination_topic,
                 schema, is_key=False):
        self.schema_registry_client = schema_registry_client
        self.destination_topic = destination_topic
        self.schema = schema
        self.is_key = is_key

        # Initialize parents
        MessageSerializer.__init__(self, schema_registry_client)
        Codec.__init__(self)

    def _loads(self, s: bytes) -> Dict:
        return self.decode_message(s)

    def _dumps(self, obj: Dict) -> bytes:
        return self.encode_record_with_schema(
            topic=self.destination_topic,
            schema=self.schema,
            record=obj,
            is_key=self.is_key
        )