import logging
from example.utils.config_base import ConfigBase

logger = logging.getLogger(__name__)


class VideoConfig(ConfigBase):
    def __init__(self):
        super().__init__()
        self.source_topic = "yt_video"
        self.id_field_name = "yt_video_id"
        self.output_record_key = "yt_video_id"
