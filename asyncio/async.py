import asyncio

async def worker():
  print('worker started.')
  await asyncio.sleep(2)
  print('worker ended.')

async def main():
  print('main started.')
  await worker()
  print('main ended.')

asyncio.run(main())
