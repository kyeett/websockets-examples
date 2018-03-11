import asyncio
import aiohttp


async def print_json(result):
    print(await result.json())


async def consul_services(url, callback=None, path='/v1/catalog/services'):
    full_url = url + path
    async with aiohttp.ClientSession() as session:
        await asyncio.sleep(0.1)
        resp = await session.get(full_url, params=consul_services.params, timeout=None)

        # Do something with resp
        if callback:
            await callback(resp)
        consul_services.params = {'index': resp.headers['X-Consul-Index']}
        return resp
consul_services.params = {}


async def loop_async(func, **args):
    while True:
        await func(**args)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(loop_async(consul_services, url='http://localhost:8500', callback=print_json))