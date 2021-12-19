import time
from datetime import datetime, timedelta, timezone

s = int(time.time())
ms = int(time.time() * 1000)
print(s)
print(ms)

# timestamp
now = datetime.now()
type(now) # <class 'datetime.datetime'>
timestamp = now.timestamp() # 1639887619.938868
now = datetime.fromtimestamp(timestamp)

# date format
date_format = '%Y%m%d %H:%M:%S'
now_str = now.strftime(date_format)
now = datetime.strptime(now_str, date_format)

# date offset
now += timedelta(days=1, hours=12)

# timezone
# get utc date
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# convert to beijing timezone.
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
