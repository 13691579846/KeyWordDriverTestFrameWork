
import logging
import time
from config.VarConfig import *

class Logger(object):
    '''
    封装的日志模块
    '''
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        """

        :param logger:
        :param CmdLevel:
        :param FileLevel:
        """
        try:
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
            # 日志输出格式
            fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
            # 日志文件名称
            # self.LogFileName = os.path.join(conf.log_path, "{0}.log.txt".format(time.strftime("%Y-%m-%d")))# %H_%M_%S
            currTime = time.strftime("%Y-%m-%d")
            self.LogFileName = logPath+currTime+'.txt'
            # 设置控制台输出
            # sh = logging.StreamHandler()
            # sh.setFormatter(fmt)
            # sh.setLevel(CmdLevel)# 日志级别

            # 设置文件输出
            fh = logging.FileHandler(self.LogFileName)
            fh.setFormatter(fmt)
            fh.setLevel(FileLevel)# 日志级别

            # self.logger.addHandler(sh)
            self.logger.addHandler(fh)
        except Exception as e:
            raise e

if __name__ == '__main__':
    logger = Logger("fox",CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    logger.logger.debug("debug")
    logger.logger.log(logging.ERROR,'%(module)s %(info)s',{'module':'log日志','info':'error'}) #ERROR,log日志 error
