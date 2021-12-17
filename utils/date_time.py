import time
from datetime import datetime

s = int(time.time())
ms = int(time.time() * 1000)
print(s)
print(ms)

now = datetime.now()
now = datetime.fromtimestamp(now.timestamp())

print(now.strftime("%Y%m%d %H:%M:%S"))	
