import logging
from os import path
from ..app.settings import BASE_DIR


def logger(file_path: str):
    logger = logging.getLogger(file_path.split('.')[0])
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
    file_handler = logging.FileHandler(path.join(BASE_DIR, 'logger', file_path))
    file_handler.formatter = formatter
    logger.addHandler(file_handler)
    return logger

