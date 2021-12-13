import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{time:HH:mm:ss}| {message}")
logger.add("tmp/example.log", format="{time:MM-DD HH:mm:ss}| {level}| {message}")

def log(*args, error=False):
  fn = logger.error if error else logger.info
  strs = [str(arg) for arg in args]
  fn(' '.join(strs))
  