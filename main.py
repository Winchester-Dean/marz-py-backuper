import os
import asyncio
import logging

from dispatcher import dp, bot
from handlers import *

logging.basicConfig(level=logging.INFO)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    asyncio.run(main())
