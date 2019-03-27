import win32api
import win32con

class KeyBoardKeys(object):
    '''
    模拟键盘
    '''
    # 键盘编码
    vk_code ={
        'enter':0x0D,
        'tab' : 0x09,
        'ctrl':0x11,
        'v':0x56
    }
    @staticmethod
    def keyDown(keyName):
        '''
        模拟按下键
        :param keyName:
        :return:
        '''
        try:
            win32api.keybd_event(KeyBoardKeys.vk_code[keyName],0,0,0)
        except Exception as e:
            raise e
    @staticmethod
    def keyUp(keyName):
        '''
        释放键
        :param keyName:
        :return:
        '''
        try:
            win32api.keybd_event(KeyBoardKeys.vk_code[keyName],0,win32con.KEYEVENTF_KEYUP,0)
        except Exception as e:
            raise e
    @staticmethod
    def oneKey(key):
        '''
        模拟当个按键
        :param key:
        :return:
        '''
        try:
            KeyBoardKeys.keyDown(key)
            KeyBoardKeys.keyUp(key)
        except Exception as e:
            raise e

    @staticmethod
    def twoKeys(key1, key2):
        '''
        模拟组合按键
        :param key1:
        :param key2:
        :return:
        '''
        try:
            KeyBoardKeys.keyDown(key1)
            KeyBoardKeys.keyDown(key2)
            KeyBoardKeys.keyUp(key1)
            KeyBoardKeys.keyUp(key2)
        except Exception as e:
            raise e

if __name__=='__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python')
    KeyBoardKeys.oneKey('enter')
