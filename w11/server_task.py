import asyncio
import aiohttp


async def get_resp(url: str, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as resp:  # Getting info from the site with ".get()"
        print(await resp.text())


async def worker(num: int) -> None:
    async with aiohttp.ClientSession() as session:
        responses = [get_resp('http://127.0.0.1:8000', session) for _ in range(num)]
        await asyncio.gather(*responses)


if __name__ == "__main__":
    asyncio.run(worker(10))
