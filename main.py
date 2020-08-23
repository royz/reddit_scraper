import sys
import logging
from logging.handlers import RotatingFileHandler


def get_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=(
            RotatingFileHandler(
                filename='logs.log',
                maxBytes=(1024 ** 3) / 2,  # max log file size 512MB
                backupCount=1,
            ),
            logging.StreamHandler(sys.stdout)
        )
    )
    return logging.getLogger()


if __name__ == '__main__':
    logger = get_logger()
