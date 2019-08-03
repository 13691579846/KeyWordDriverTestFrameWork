"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : ObjectMap.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time


def get_element(driver, by, locator):
    """查找单一元素"""
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return element


def get_elements(driver, by, locator):
    """获取一组元素"""
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return elements


if __name__ == "__main__":
    d = webdriver.Firefox()
    d.get('https://mail.126.com')
    time.sleep(5)
    d.switch_to.frame(get_element(d, 'xpath', "//div[@id='loginDiv']/iframe"))
    username = get_element(d, 'xpath', "//input[@name='email']")
    username.send_keys('linuxxiaochao')
    d.switch_to.default_content()
    d.quit()
