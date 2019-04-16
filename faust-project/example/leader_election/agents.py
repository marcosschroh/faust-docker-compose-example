import random
import logging

from example.app import app

logger = logging.getLogger(__name__)


@app.agent()
async def say(greetings):
    async for greeting in greetings:
        logger.info(greeting)


@app.timer(4.0, on_leader=True)
async def publish_greetings():
    logger.info('PUBLISHING ON LEADER!')
    greeting = str(random.random())
    await say.send(value=greeting, value_serializer='raw')
