"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : KeyBoardUtil.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import win32api
import win32con
from selenium import webdriver


class KeyBoardKeys(object):
    """模拟键盘"""
    # 键盘编码
    vk_code = {
        'enter': 0x0D,
        'tab': 0x09,
        'ctrl': 0x11,
        'v': 0x56
    }

    @staticmethod
    def key_down(key_name):
        """模拟按下键"""
        try:
            win32api.keybd_event(KeyBoardKeys.vk_code[key_name], 0, 0, 0)
        except Exception as e:
            raise e

    @staticmethod
    def key_up(key_name):
        """释放键"""
        try:
            win32api.keybd_event(KeyBoardKeys.vk_code[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)
        except Exception as e:
            raise e

    @staticmethod
    def one_key(key):
        """模拟单个按键"""
        try:
            KeyBoardKeys.key_down(key)
            KeyBoardKeys.key_up(key)
        except Exception as e:
            raise e

    @staticmethod
    def two_keys(key1, key2):
        """模拟组合按键"""
        try:
            KeyBoardKeys.key_down(key1)
            KeyBoardKeys.key_down(key2)
            KeyBoardKeys.key_up(key1)
            KeyBoardKeys.key_up(key2)
        except Exception as e:
            raise e


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python')
    KeyBoardKeys.one_key('enter')
