import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{time:HH:mm:ss}| {message}")
logger.add("tmp/example.log", format="{time:MM-DD HH:mm:ss}| {level}| {message}")

logger.debug("Log1")
logger.error("Log2")

# @logger.catch
# def f1():
#   1/0
# f1()