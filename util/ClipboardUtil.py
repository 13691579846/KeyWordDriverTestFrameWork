import win32clipboard as w
import win32con

class Clipboard(object):

    @staticmethod
    def getText():
        '''
        获取剪切板的内容
        :return:
        '''

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
    def setText(value):
        '''
        设置剪切板内容
        :return:
        '''
        try:
            w.OpenClipboard()# 打开剪切板
            w.EmptyClipboard()# 清空剪切板
            w.SetClipboardData(win32con.CF_UNICODETEXT, value) # 设置内容
            w.CloseClipboard() # 关闭
        except Exception as e:
            raise e

if __name__=='__main__':
    from selenium import webdriver

    value = 'python'
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    query = driver.find_element_by_id('kw')
    Clipboard.setText(value)
    clValue = Clipboard.getText()
    query.send_keys(clValue.decode('utf-8'))
