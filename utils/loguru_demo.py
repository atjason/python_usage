import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{time:HH:mm:ss}| {message}")
logger.add("tmp/example.log", format="{time:MM-DD HH:mm:ss}| {level}| {message}")

logger.debug("Log1")
logger.error("Log2")

def log(*args):
  strs = [str(arg) for arg in args]
  logger.info(' '.join(strs))

log(1)
log(1, 2)

# @logger.catch
# def f1():
#   1/0
# f1()