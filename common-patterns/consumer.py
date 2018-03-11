#!/bin/env python
# Examples taken from: http://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import websockets
import os
from random import randint

port = int(os.environ.get('PORT', '8765'))
host = os.environ.get('HOST', '')


async def consumer(message):
    timer = randint(0, 5) / 10
    print("Sleeping for %s seconds" % timer)
    await asyncio.sleep(timer)
    print(message)


async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)


start_server = websockets.serve(consumer_handler, host, port)
asyncio.get_event_loop().run_until_complete(start_server)

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt as e:
    print("\nShutting down server")
