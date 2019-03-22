from selenium.webdriver.support.wait import WebDriverWait


def getElement(driver, by, locator):
    '''
    查找单一元素
    :param driver:
    :param by:
    :param locator:
    :return: 元素对象
    '''
    try:
        element = WebDriverWait(driver, 30).until(lambda x : x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return element

def getElements(driver, by, locator):
    '''
    获取一组元素
    :param driver:
    :param by:
    :param locator:
    :return: 一组元素对象
    '''
    try:
        elements = WebDriverWait(driver, 30).until(lambda x : x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return elements


if __name__=="__main__":
    from selenium import webdriver
    import time

    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    time.sleep(5)
    driver.switch_to.frame(getElement(driver, 'xpath', "//div[@id='loginDiv']/iframe"))
    username = getElement(driver, 'xpath', "//input[@name='email']")
    username.send_keys('linuxxiaochao')
    driver.switch_to.default_content()
    driver.quit()