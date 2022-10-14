import logging


logging.basicConfig(filename='dev.log',level=logging.DEBUG, format="%(name)s %(asctime)s %(levelname)s  :  %(message)s %(filename)s %(funcName)s ln: ( %(lineno)s )")

logging.info('hello')
logger1=logging.getLogger(__name__)
logging.addLevelName
handler=logging.FileHandler('x.log')
handler.setFormatter
logger1.addHandler(handler)

logger1.info('hiiii')