import logging
import logging.config

import faust

from example import SETTINGS

logger = logging.getLogger(__name__)


KAFKA_BROKER = SETTINGS.get("confluent", "bootstrap.server")

app = faust.App(
    version=1,
    autodiscover=True,
    origin='example',
    id="1",
    broker=KAFKA_BROKER,
)


def main() -> None:
    app.main()
