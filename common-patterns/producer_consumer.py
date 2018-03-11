#!/bin/env python
# Examples taken from: http://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import websockets
import os
from random import randint

port = int(os.environ.get('PORT', '8765'))
host = os.environ.get('HOST', '')


async def producer():
    producer.c += 1
    timer = randint(5, 10) / 10
    await asyncio.sleep(timer)
    return "Server message #{}".format(producer.c)

producer.c = 0


async def producer_handler(websocket, path):
    message = await producer()
    await websocket.send(message)
    print("> {}".format(message))


async def consumer(message):
    print("< {}".format(message))


async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)


async def handler(websocket, path):

    while True:
        consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
        producer_task = asyncio.ensure_future(producer_handler(websocket, path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()


start_server = websockets.serve(handler, host, port)
asyncio.get_event_loop().run_until_complete(start_server)

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt as e:
    print("\nShutting down server")
