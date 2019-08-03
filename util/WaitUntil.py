"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : WaitUntil.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

from util.ObjectMap import get_element


class WaitUnit(object):
    def __init__(self, driver):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def presence_of_element_located(self, by, locator):
        """显示等待某个元素出现在dom中，不一定可见，存在返回元素对象"""
        try:
            if by.lower() in self.byDic:
                self.wait.until(ec.presence_of_element_located((self.byDic[by.lower()], locator)))
            else:
                raise TypeError('未找到定位方式,请确保定位方式正确')
        except Exception as e:
            raise e

    def frame_to_be_available_and_switch_to_it(self, by, locator):
        """检查frame是否存在，存在就切换到frame中"""
        try:
            if by.lower() in self.byDic:
                self.wait.until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by.lower()], locator)))
            else:
                raise TypeError('未找到定位方式,请确保定位方式正确')
        except Exception as e:
            raise e

    def visibility_of_element_located(self, by, locator):
        """显示等待页面元素出现在dom中， 并且可见， 存在则返回该元素对象"""
        try:
            if by.lower() in self.byDic:
                self.wait.until(ec.visibility_of_element_located((self.byDic[by.lower()], locator)))
            else:
                raise TypeError('未找到定位方式,请确保定位方式正确')
        except Exception as e:
            raise e


if __name__ == '__main__':
    d = webdriver.Firefox()
    d.get('https://mail.126.com')
    wait = WaitUnit(d)
    wait.frame_to_be_available_and_switch_to_it('xpath', "//div[@id='loginDiv']/iframe")
    wait.visibility_of_element_located('xpath', "//input[@name='email']")
    u_name = get_element(d, 'xpath', "//input[@name='email']")
    u_name.send_keys('python')
    d.quit()
