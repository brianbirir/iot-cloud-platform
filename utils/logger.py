import logging

# logging
logger = logging.getLogger('ruleblox_broker')
hdlr = logging.FileHandler('/var/tmp/ruleblox_broker.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)


# log INFO
def info_logger(message):

    logger.setLevel(logging.INFO)
    logger.info(message)


# log ERROR
def error_logger(message):

    logger.setLevel(logging.ERROR)
    logger.error(message)