import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        print(f"Async call {num}")
        await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org")
        print(response)


def http_call_sync():
    for num in range(1, 6):
        print(f"Sync call {num}")
        sleep(1)
    response = httpx.get("https://httpbin.org")
    print(response)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Async view response")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Sync view response")
