from example.utils.avro.serializer.message_serializer import MessageSerializer
from faust.serializers.codecs import Codec

from typing import Dict


class FaustAvroSerializer(MessageSerializer, Codec):
    """
    Subclass of Faust serde Codec that uses Confluent-Kafka's MessageSerializer
    for its decode and encode interfaces
    """

    def __init__(self, schema_registry_client=None, destination_topic=None,
                 schema=None, is_key=False):
        self.schema_registry_client = schema_registry_client
        self.destination_topic = destination_topic
        self.schema = schema
        self.is_key = is_key
        MessageSerializer.__init__(self, registry_client=self.schema_registry_client)
        Codec.__init__(self)

    def _loads(self, s: bytes) -> Dict:
        return self.decode_message(s)

    def _dumps(self, obj: Dict) -> bytes:
        # return self.encode_record_with_schema()
        return self.encode_record_with_schema(topic=self.destination_topic,
                                              schema=self.schema,
                                              record=obj,
                                              is_key=self.is_key)
