import logging

from example.app import app
from example.codecs.avro import avro_user_serializer
from example.users.models import UserModel

users_topic = app.topic('avro_users', partitions=1, value_type=UserModel)

logger = logging.getLogger(__name__)


@app.agent(users_topic)
async def users(users):
    async for user in users:
        logger.info("Event received in topic avro_users")
        logger.info(f"First Name: {user.first_name}, last name {user.last_name}")


@app.timer(5.0, on_leader=True)
async def publish_users():
    logger.info('PUBLISHING ON LEADER FOR USERS APP!')
    user = {"first_name": "foo", "last_name": "bar"}
    await users.send(value=user, value_serializer=avro_user_serializer)
