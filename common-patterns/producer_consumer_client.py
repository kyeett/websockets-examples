#!/usr/bin/env python

import asyncio
import websockets
import os

port = int(os.environ.get('PORT', '8765'))


async def hello():
    print("Starting client on :%s" % port)
    async with websockets.connect('ws://localhost:%s' % port) as websocket:

        msg = 'Client msg #1'
        await websocket.send(msg)
        print('> {}'.format(msg))

        i = 0
        while True:
            greeting = await websocket.recv()
            i += 1
            print("< {}".format(greeting))


asyncio.get_event_loop().run_until_complete(hello())
