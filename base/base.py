from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化操作
    def __init__(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        # 必填，而且正确
        desired_caps['platformName'] = 'android'
        # 可以不添加键值对，如果添加就一定要正确。 必填且正确
        desired_caps['platformVersion'] = '5.1'
        # 可以写错，但不能为空
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 扩展：启动时直接安装apk文件 ，可以忽略 包名和启动名
        desired_caps['appPackage'] = "com.vcooline.aike"
        # 启动名：
        desired_caps['appActivity'] = '.umanager.LoginActivity'
        # 获取driver
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()
