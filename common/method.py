# 导入appium
from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.faker_data import Fake
import random


def open_app():
    # 2.配置启动参数
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": ".activity.EcmobileMainActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }
    # 3.启动app
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    sleep(3)
    return driver


class Base:
    def __init__(self, driver):
        self.driver = driver
        # 获取手机屏幕大小(分辨率)
        size = self.driver.get_window_size()
        self.width = size["width"]  # 获取手机宽度
        self.height = size["height"]  # 获取手机高度

    def open_app(self):
        '''打开app'''
        self.driver = open_app()

    def swipe_up(self, time=5000):
        """
        向上滑动:y坐标从大到小
        :return:
        """
        x = self.width * 0.5
        start_y = self.height * 0.75  # y坐标起始值
        end_y = self.height * 0.25  # y坐标终止值
        self.driver.swipe(x, start_y, x, end_y, duration=time)

    def swipe_down(self, time=5000):
        """
        向下滑动:y坐标从小到大
        :return:
        """
        x = self.width * 0.5
        start_y = self.height * 0.25  # y坐标起始值
        end_y = self.height * 0.75  # y坐标终止值
        self.driver.swipe(x, start_y, x, end_y, duration=time)

    def swipe_left(self, time=5000):
        """
        向左滑动:x坐标从大到小
        :return:
        """
        start_x = self.width * 0.75  # x起始位置
        end_x = self.width * 0.25  # x终止位置
        y = self.height * 0.5
        self.driver.swipe(start_x, y, end_x, y, duration=time)

    def swipe_right(self, time=5000):
        """
        向右滑动:x坐标从小到大
        :return:
        """
        start_x = self.width * 0.25  # x起始位置
        end_x = self.width * 0.75  # x终止位置
        y = self.height * 0.5
        self.driver.swipe(start_x, y, end_x, y, duration=time)

    def find_element(self, locator: tuple = None, timeout=10):
        '''元素定位'''
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def click(self, locator):
        '''元素点击'''
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        '''元素输入'''
        element = self.find_element(locator)
        element.send_keys(text)

    def close_app(self):
        '''关闭app'''
        self.driver.quit()

    def get_element_file(self, locator):
        """
        获取元素文本
        :return:
        """
        try:
            element = self.find_element(locator)
            return element.text
        except:
            return False

    def find_elements(self, locator, timeout=5):
        '''
        定位一组元素,如果找到,返回一组元素,反之返回一个False
        :param locator: 定位器
        :param timeout: 最大的等待时间
        :return: elements
        '''
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def get_goods_num(self, locator):
        '''获取所有商品并获取长度'''
        try:
            goods_num = self.find_elements(locator)
            return len(goods_num)
        except:
            return 0

    def click_random_elements(self, locator):
        '''定位多个元素,并且随机选择一个'''
        element = self.find_elements(locator)
        long_num = len(element)
        n = random.randint(0, long_num - 1)
        element[n].click()


if __name__ == '__main__':
    pass
