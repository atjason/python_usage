import asyncio
from datetime import datetime

async def sub_fn1():
  for _ in range(5):
    print('sub_fn1', datetime.now())
    await asyncio.sleep(1)

async def sub_fn2():
  for _ in range(2):
    print('sub_fn2', datetime.now())
    await asyncio.sleep(2)

async def main():
  tasks = [sub_fn1(), sub_fn2()]
  await asyncio.wait(tasks)

asyncio.run(main())
