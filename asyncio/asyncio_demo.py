# https://docs.python.org/3/library/asyncio.html

import asyncio
from datetime import datetime

async def fn():
  print(1)

async def main():
  # print(datetime.now())
  # await asyncio.sleep(2)
  # print(datetime.now())
  loop = asyncio.get_running_loop()
  end_time = loop.time() + 5.0
  while True:
    print(datetime.now())
    if loop.time() + 1.0 > end_time:
      break
    await asyncio.sleep(1)

asyncio.run(main())