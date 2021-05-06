import logging


class baseclass:
    def test_logging(self):
        logger = logging.getLogger(__name__)

        logfile = logging.FileHandler('logfile.log')

        formater = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s: %(message)s")
        logfile.setFormatter(formater)
        logger.addHandler(logfile)
        logger.setLevel(logging.DEBUG)

        return logger