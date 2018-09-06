#conding=utf-8
from selenium import webdriver
import unittest

class chromedriver(unittest.TestCase):
    def setUp(self):
        options=webdriver.ChromeOptions()
        # 设置浏览器默认允许flash插件加载：1为默认加载， 0：禁止，1：询问，2：允许
        prefs = {
            'profile.managed_default_content_setting.image': 1,
            'profile.content_settings.whitelist_setting.adobe-flash-player': 1,
            'profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player': 1
        }
        options.add_experimental_option('prefs',prefs)
        self.driver=webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get('http://192.168.29.113:8888/login-web/login')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()