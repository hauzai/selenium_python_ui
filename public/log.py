import logging
import os


class MyLog:
    def __init__(self):
        self.logger = logging.getLogger("mylog")
        self.logger.setLevel(logging.DEBUG)

        __format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        __ch = logging.StreamHandler()
        __ch.setLevel(logging.DEBUG)
        __ch.setFormatter(__format)

        self.logger.addHandler(__ch)

    def debug(self, message):
        self.logger.debug(message)



