import asyncio
from datetime import datetime
import aiohttp
import ssl
import certifi
import pytz

from utils import send_to_telegram
from constants import URL


class Parse:
        def __init__(self, link):
                self.link = link
 
        async def parse_info(self):
            """ Метод для выполнения запроса и отправки данных в Telegram."""

            ssl_context = ssl.create_default_context(cafile=certifi.where())
            async with aiohttp.ClientSession() as session:
                async with session.get(self.link, ssl=ssl_context) as response:
                    if response.status == 200:
                        data = await response.json()
                        cet = pytz.timezone('CET')
                        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                        message = f'⌛️ Latest Update: {current_time}\n\n' \
                              f'⚙️ Network: {data["result"]["node_info"]["network"]}\n' \
                              f'🎚 Version: {data["result"]["node_info"]["version"]}\n' \
                              f'🔍 Latest_block_height: {data["result"]["sync_info"]["latest_block_height"]}\n' \
                              f'📝 Latest_block_time: {data["result"]["sync_info"]["latest_block_time"]}\n' \
                        # print(message)
                        send_to_telegram(message)
                    else:
                        print(f'Error: {response.status}')
        
        async def schedule_requests(self):
            """Метод для выполнения запросов с определенной периодичностью."""
            while True:
                await self.parse_info()
                await asyncio.sleep(30)


if __name__ == "__main__":
    parser = Parse(URL)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parser.schedule_requests())