import asyncio
import aiofile
import aiohttp


async def fetch(client, service):
    async with client.get(service) as resp:
        text = await resp.text()

        for line in text:
            if line.startswith('a '):
                async with aiofile.AIOFile('found.txt', 'w') as file:
                    await file.write(f'From: {service}\nWhat: {line} \n')


async def async_read(file_name):
    async with aiofile.AIOFile(file_name, 'r') as f:
        async with aiohttp.ClientSession() as session:
            async for line in aiofile.LineReader(f):
                await asyncio.ensure_future(fetch(session, line))


if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(async_read('urls.txt'))
