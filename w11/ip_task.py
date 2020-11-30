from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
import socket

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service, session):
    async with session.get(service.url):
        hostname = socket.gethostname()  # Get the hostname using the socket.gethostname() method
        # Find the IP address by passing the hostname as an argument to the
        return socket.gethostbyname(hostname)  # socket.gethostbyname() method



async def asynchronous():
    async with aiohttp.ClientSession() as session:
        done, pending = await asyncio.wait({fetch_ip(service, session) for service in SERVICES},
                                           return_when=FIRST_COMPLETED)
        for serv in done:
            print(serv.result())

if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asynchronous())
