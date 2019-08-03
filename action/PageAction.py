"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : PageAction.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from config.VarConfig import iePath, chromePath
from util.DirAndTime import DirAndTime
from util.ObjectMap import get_element
from util.ClipboardUtil import Clipboard
from util.KeyBoardUtil import KeyBoardKeys
from util.WaitUntil import WaitUnit

from selenium import webdriver

driver = None
waitUtil = None


# 打开浏览器
def open_browser(browser):
    global driver, waitUtil
    try:
        if browser.lower() == 'ie':
            driver = webdriver.Ie(executable_path=iePath)
        elif browser.lower() == 'chrome':
            driver = webdriver.Chrome(executable_path=chromePath)
        else:
            # driver = webdriver.Firefox(executable_path=fireFox)
            driver = webdriver.Firefox()
    except Exception as e:
        raise e
    else:
        waitUtil = WaitUnit(driver)  # driver 创建之后， 创建等待类实例对象


# 浏览器窗口最大化
def maximize_browser():
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


# 加载网址
def load_url(url):
    try:
        driver.get(url)
    except Exception as e:
        raise e


# 强制等待
def sleep(num):
    try:
        import time
        time.sleep(num)
    except Exception as e:
        raise e


# 清除输入框的内容
def clear(by, locator):
    try:
        get_element(driver, by, locator).clear()
    except Exception as e:
        raise e


# 输入框中输入内容
def input_value(by, locator, value):
    try:
        element = get_element(driver, by, locator)
        # element.click()
        element.send_keys(value)
    except Exception as e:
        raise e


# 点击操作
def click_btn(by, locator):
    try:
        get_element(driver, by, locator).click()
    except Exception as e:
        raise e


# 断言页面的title
def assert_title(title):
    try:
        assert title in driver.title, "%s not found in title!" % title
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


# 断言目标字符串是否包含在页面源码中
def assert_string_in_page_source(string):
    try:
        assert string in driver.page_source, "%s not found in page source!" % string
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def assert_error_info(by, locator, string):
    element = get_element(driver, by, locator)
    text = element.text
    assert text == string


# 获取当前页面的title
def get_title():
    try:
        return driver.title
    except Exception as e:
        raise e


# 获取页面源码
def get_page_source():
    try:
        return driver.page_source
    except Exception as e:
        raise e


# 切换到frame里面
def switch_to_frame(by, locator):
    try:
        driver.switch_to.frame(get_element(driver, by, locator))
    except Exception as e:
        raise e


# 跳到默认的frame
def switch_to_default():
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e


# 模拟ctrl+v键
def ctrl_v(value):
    try:
        Clipboard.set_text(value)
        sleep(2)
        KeyBoardKeys.two_keys('ctrl', 'v')
    except Exception as e:
        raise e


# 模拟tab键
def tab_key():
    try:
        KeyBoardKeys.one_key('tab')
    except Exception as e:
        raise e


# 模拟enter键
def enter_key():
    try:
        KeyBoardKeys.one_key('enter')
    except Exception as e:
        raise e


# 屏幕截图
def save_screen_shot():
    picture_name = DirAndTime.create_picture_path() + '\\' + DirAndTime.get_current_time() + '.png'
    try:
        driver.get_screenshot_as_file(picture_name)
    except Exception as e:
        raise e
    else:
        return picture_name


def wait_presence_of_element_located(by, locator):
    """显示等待页面元素出现在DOM中，单并不一定可见"""
    waitUtil.presence_of_element_located(by, locator)


def wait_frame_to_be_available_and_switch_to_it(by, locator):
    """检查frame是否存在，存在就切换到frame中"""
    waitUtil.frame_to_be_available_and_switch_to_it(by, locator)


def wait_visibility_of_element_located(by, locator):
    """显示等待页面元素出现在DOM中，并且可见"""
    waitUtil.visibility_of_element_located(by, locator)


# 关闭浏览器
def quit_browser():
    try:
        driver.quit()
    except Exception as e:
        raise e


if __name__ == '__main__':
    open_browser('firefox')
    load_url('http://www.baidu.com')
    # inputValue('id', 'kw','python')
    # clear('id', 'kw')
    # inputValue('id', 'kw', 'python')
    # clickBtn('id', 'su')
    # sleep(3)
    # title = getTitle()
    # print(title)
    # assertTitle('python')
    # assert_string_in_page_source('python')
    ctrl_v('python')
