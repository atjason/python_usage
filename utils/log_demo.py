# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/library/logging.html

# DEBUG
# INFO
# NOTICE
# WARNING (default)
# ERROR
# CRITICAL
# ALERT
# EMERGENCY

import logging

# Config

# Logging to a file
logging.basicConfig(filename='tmp/example.log', level=logging.INFO)

# Changing the format of displayed messages
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

logging.warning('Watch out!')
logging.info('I told you so.')

# Logging variable data
logging.warning('Hello %s.', 'Tom')
