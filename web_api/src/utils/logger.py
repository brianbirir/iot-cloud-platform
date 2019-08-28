"""This helper module logs messages of different severity levels
"""
import logging
from config import Config

cnf = Config()


logger = logging.getLogger('ruleblox_api')
app_log_handler = logging.FileHandler(cnf.LOGGING_FILE)
app_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
app_log_handler.setFormatter(app_log_formatter)
logger.addHandler(app_log_handler)


def info(message):
    logger.setLevel(logging.INFO)
    logger.info(message)


def error(message):
    logger.setLevel(logging.ERROR)
    logger.error(message)


def warning(message):
    logger.setLevel(logging.WARNING)
    logger.warning(message)
