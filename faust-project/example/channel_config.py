from example.utils.config_base import ConfigBase


class ChannelConfig(ConfigBase):
    def __init__(self):
        super().__init__()
        self.source_topic = "yt_channel"
        self.id_field_name = "yt_channel_id"
        self.output_record_key = "yt_channel_id"
