import aiohttp
import asyncio

async def fetch():
    url = "http://google.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                print(content)
            else:
                print(f"Failed to fetch the page. Status code: {response.status}")

# Run the async function
asyncio.run(fetch())
