import logging
def test_logging():

    logger = logging.getLogger(__name__)

    logfile = logging.FileHandler('logfile.log')

    formater = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s: %(message)s")
    logfile.setFormatter(formater)
    logger.addHandler(logfile)
    logger.setLevel(logging.DEBUG)

    logger.debug("debug statement")
    logger.info("information message")
    logger.warning("Warings")
    logger.error("A major error is happen")
    logger.critical("critical issue")