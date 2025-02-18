from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys



# logging.info("welcome to us_visa")

# logging.info("welcome to us_visa susant experiment")

# logging.info("welcome to us_visa experiment")


# logging.info("welcome to us_visa experiment susant")

try:
    a = 2/0
except Exception as e:
    logging.error(USvisaException(str(e), sys))











