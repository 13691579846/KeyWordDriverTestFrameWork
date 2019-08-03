"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : ClipboardUtil.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import win32clipboard as w
import win32con
from selenium import webdriver


class Clipboard(object):

    @staticmethod
    def get_text():
        """获取剪切板的内容"""
        try:
            # 打开剪切板
            w.OpenClipboard()
            # 读取数据
            value = w.GetClipboardData(win32con.CF_TEXT)
            # 关闭剪切板
            w.CloseClipboard()
        except Exception as e:
            raise e
        else:
            return value

    @staticmethod
    def set_text(value):
        """设置剪切板内容"""
        try:
            w.OpenClipboard()  # 打开剪切板
            w.EmptyClipboard()  # 清空剪切板
            w.SetClipboardData(win32con.CF_UNICODETEXT, value)  # 设置内容
            w.CloseClipboard()  # 关闭
        except Exception as e:
            raise e


if __name__ == '__main__':
    data = 'python'
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    query = driver.find_element_by_id('kw')
    Clipboard.set_text(data)
    clValue = Clipboard.get_text()
    query.send_keys(clValue.decode('utf-8'))
