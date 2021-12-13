import sys
from loguru import logger
from logger import log

logger.debug("Log1")
logger.error("Log2")

log(1)
log(1, 2)
log(1, 2, 3, error=True)

# @logger.catch
# def f1():
#   1/0
# f1()