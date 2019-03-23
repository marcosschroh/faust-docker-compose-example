import random

from example.app import app


@app.agent()
async def say(greetings):
    async for greeting in greetings:
        print(greeting)


@app.timer(4.0, on_leader=True)
async def publish_greetings():
    print('PUBLISHING ON LEADER!')
    greeting = str(random.random())
    await say.send(value=greeting, value_serializer='raw')
