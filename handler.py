import logging
import sys

def lambda_handler(event, context):
    logger = logging.getLogger('test')

    # https://forum.serverless.com/t/python-lambda-logging-duplication-workaround/1585
    logging.getLogger().handlers = []

    h = logging.StreamHandler(sys.stdout)

    # use whatever format you want here
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    h.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)


    logger.info('Starting lambda function...')

    logger.info('end of lambda function')

    return True