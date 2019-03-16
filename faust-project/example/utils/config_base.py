from typing import Any, Dict
from pkg_resources import iter_entry_points


def load_config(config_class: str):
    return next(iter_entry_points('configs', config_class)).load()


class ConfigBase:
    def __init__(self):
        self.consumer_name = None
        self.source_topic = None
        self.output_topic = None
        self.output_value_schema = None
        self.output_key_schema = None
        self.id_field_name = None
        self.output_record_key = None

    def get_avro_key(self, record: Dict[Any, Any]) -> Dict[str, Any]:
        return {self.id_field_name: record.get(self.output_record_key)}
