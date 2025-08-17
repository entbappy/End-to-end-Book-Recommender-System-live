from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
import sys


try:
    output = 4/0
    print(output)
except Exception as e:
    logging.info(e)
    raise AppException(e, sys) from e