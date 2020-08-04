import logging

logging.basicConfig(filename='newfile.log',
                    format='%(asctime)s :: %(levelname)s :: %(message)s',filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("I am debugging")
logger.info("I am Info")
logger.warning("Its just a warning")
logger.error("I am an error")
