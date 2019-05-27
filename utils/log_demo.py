# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/library/logging.html

# The default level is WARNING

import logging

# Config

# Logging to a file
# logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Changing the format of displayed messages
# logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

logging.warning('Watch out!')
logging.info('I told you so.')

# Logging variable data
logging.warning('Hello %s.', 'Tom')
