import logging


class Logger:
    __register = False

    def __init__(self):
        if not self.__register:
            self._init_default_register()

    def _init_default_register(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        Logger.__register = True
        logging.info("Logger initialized")

    def get_logger(self, filename):
        return logging.getLogger(filename)


def log(cls):
    cls.logger = Logger().get_logger(cls.__name__)
    return cls
