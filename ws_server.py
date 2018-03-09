#!/usr/bin/env python
import asyncio

import websockets
import os

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))


port = int(os.environ.get('PORT','8765'))
print("Starting server on :%s" % port)

start_server = websockets.serve(hello, 'localhost', port)
asyncio.get_event_loop().run_until_complete(start_server)

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt as e:
    print("\nShutting down server")
