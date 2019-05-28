import asyncio
import threading
from datetime import datetime

async def main_fn():
  for _ in range(5):
    await asyncio.sleep(1)
    print('main_fn:', datetime.now())

async def sub_fn():
  for _ in range(5):
    await asyncio.sleep(1.001)
    print('sub_fn: ', datetime.now())

def loop_in_thread(loop):
  asyncio.set_event_loop(loop)
  loop.run_until_complete(sub_fn())
  
loop = asyncio.get_event_loop()
t = threading.Thread(target=loop_in_thread, args=(loop,))
t.start()

asyncio.run(main_fn())
