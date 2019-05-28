import asyncio
from datetime import datetime

async def fn(name):
  for _ in range(2):
    print(name, datetime.now())
    await asyncio.sleep(2)

async def main():
  task1 = asyncio.create_task(fn('A'))
  task2 = asyncio.create_task(fn('B'))
  done, pending = await asyncio.wait([task1, task2], return_when=asyncio.ALL_COMPLETED)
  if task1 not in done:
    print('task1 not done.')
  len(pending) == 0

asyncio.run(main())
