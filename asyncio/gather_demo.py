import asyncio
from datetime import datetime

async def fn(name):
  for _ in range(2):
    print(name, datetime.now())
    await asyncio.sleep(2)

async def main():
  await fn('A')
  await fn('B')
  
  await asyncio.gather(
    fn('1'),
    fn('2'),
  )

asyncio.run(main())
