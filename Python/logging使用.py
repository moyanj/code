# import logging
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")


import logging
logging.basicConfig(
        filename="log.txt",
        filemode="w",
        level = logging.INFO,
        format='%(asctime)s - %(filename)s[%(funcName)s, line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger()


def test():

    logger.info("test1-1")
    logger.info("test1-2")

def test2():
    logger.info("test2-1")
    logger.info("test2-2")

if __name__ == "__main__":
    test()
    test2()