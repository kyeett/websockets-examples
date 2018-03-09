#!/usr/bin/env python

import asyncio
import websockets
import os

port = int(os.environ.get('PORT', '8765'))
print("Starting client on :%s" % port)


async def hello():
    async with websockets.connect('ws://localhost:%s' % port) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())