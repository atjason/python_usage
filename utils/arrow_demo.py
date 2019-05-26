# https://arrow.readthedocs.io

import arrow
from datetime import datetime

# Creation
arrow.utcnow() # <Arrow [2019-05-26T09:17:50.251399+00:00]>
arrow.now() # <Arrow [2019-05-26T17:17:52.683387+08:00]>
arrow.now('America/New_York') # <Arrow [2019-05-26T05:18:41.305204-04:00]>

arrow.get(1558862400)
arrow.get('1558862400')
arrow.get(1558862400.0)

arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
arrow.get('2013-05-05T12:30:45')

# Properties
a = arrow.now()
a.datetime
a.timestamp
a.year # etc

# Replace & shift
a = arrow.now()
a.replace(hour=4)
a.replace(tzinfo='America/New_York')
a.shift(hours=1)
a.shift(hours=-1)

# Format
a = arrow.now()
a.format('YYYY-MM-DD HH:mm:ss')

# Convert
utc = arrow.utcnow()
utc.to('local').to('utc')
utc.to('America/New_York')

# Humanize
past = arrow.now().shift(hours=-1)
past.humanize() # 'an hour ago'
past.humanize(locale='zh_cn') # '1小时前'

# Ranges & spans
a = arrow.now()
a.span('hour') # (<Arrow [2019-05-26T17:00:00+08:00]>, <Arrow [2019-05-26T17:59:59.999999+08:00]>)
a.floor('hour')
a.ceil('hour')

# Tokens
# https://arrow.readthedocs.io/en/latest/#tokens
# YYYY/YY/MM, etc