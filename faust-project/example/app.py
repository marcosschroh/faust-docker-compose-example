import faust

from simple_settings import settings
from logging.config import dictConfig

app = faust.App(
    version=1,
    autodiscover=True,
    origin='example',
    id="1",
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    logging_config=dictConfig(settings.LOGGING),
)


def main() -> None:
    app.main()

