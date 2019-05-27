import asyncio

async def long_fn():
  await asyncio.sleep(3600)

async def main():
  try:
    await asyncio.wait_for(long_fn(), timeout=1.0)
  except asyncio.TimeoutError:
    print('Time out.')

asyncio.run(main())
