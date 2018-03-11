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
            name = input("What's your name? ")
            for i in range(repetitions):
                await websocket.send(name)
            print("> {}".format(name))

asyncio.get_event_loop().run_until_complete(hello())