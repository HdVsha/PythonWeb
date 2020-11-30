import asyncio
import aiofile
import aiohttp


async def fetch(client, service):
    async with client.get(service) as resp:
        text = resp.text()

        for line in text:
            if line.startswith('a '):
                async with aiofile.async_open('found.txt', 'a') as file:
                    file.write(f'From: {service}\n What: {line} \n')


async def async_read(file_name):
    async with aiofile.async_open(file_name, 'r') as f:
        async for line in aiofile.LineReader(f):
            async with aiohttp.ClientSession() as session:
                asyncio.ensure_future(fetch(session, line))


if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(async_read('urls.txt'))
