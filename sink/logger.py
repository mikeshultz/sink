""" Console logging functionality """
import logging
import coloredlogs

logger = logging.getLogger('sink')

coloredlogs.install(
                    level=logging.INFO,
                    fmt='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
                )

def get_logger(name):
    log = logger.getChild(name)
    return log

def set_debug_logging():
    logger.setLevel(logging.DEBUG)
    