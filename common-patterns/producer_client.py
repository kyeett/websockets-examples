#!/usr/bin/env python

import asyncio
import websockets
import os

port = int(os.environ.get('PORT', '8765'))
repetitions = int(os.environ.get('REPETITIONS', '1'))


async def hello():
    print("Starting client on :%s" % port)
    async with websockets.connect('ws://localhost:%s' % port) as websocket:

        while True:
            greeting = await websocket.recv()
            print("> {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())