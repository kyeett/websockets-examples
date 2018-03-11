import asyncio
import aiohttp


async def getgetget(url):
    params = {}
    async with aiohttp.ClientSession() as session:
        while True:
            resp = await session.get(url, params=params, timeout=None)

            # Do something with resp
            print(await resp.json())
            params = {'index': resp.headers['X-Consul-Index']}


asyncio.get_event_loop().run_until_complete(getgetget('http://localhost:8500/v1/catalog/services'))
