import logging


def display():
    logger = logging.getLogger()
    logger.info('Hello')
    logger.warning('Testing %s', 'foo')
