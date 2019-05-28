import asyncio
import concurrent.futures
from datetime import datetime

def blocking_io():
  # File operations (such as logging) can block theevent loop.
  # Run them in a thread pool.
  with open('/dev/urandom', 'rb') as f:
    f.read(1000)
    return 'done'

def cpu_bound():
  # CPU-bound operations will block the event loop:
  # In general it is preferable to run them in a process pool.
  return sum(i * i for i in range(10 ** 6))

async def sub_fn1():
  # 1. Run in the default loop's executor:
  for _ in range(5):
    print('sub_fn1', datetime.now())
    await asyncio.sleep(1)

async def sub_fn2(loop):
  # 2. Run in a custom thread pool:
  print('sub_fn2 start')

  await loop.run_in_executor(None, blocking_io)
  await loop.run_in_executor(None, cpu_bound)

  # with concurrent.futures.ThreadPoolExecutor() as pool:
  #   await loop.run_in_executor(pool, blocking_io)
  #   await loop.run_in_executor(pool, cpu_bound)

  print('sub_fn2 done')

async def main():
  loop = asyncio.get_running_loop()
  tasks = [sub_fn1(), sub_fn2(loop)]
  await asyncio.wait(tasks)

asyncio.run(main())
