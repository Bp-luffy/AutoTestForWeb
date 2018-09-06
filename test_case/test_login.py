#conding=utf-8
import unittest,time
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_login(unittest.TestCase):
    def setUp(self):
        options=webdriver.ChromeOptions()
        #设置浏览器默认允许flash插件加载：1为默认加载， 0：禁止，1：询问，2：允许
        prefs={
            'profile.managed_default_content_setting.image':1,
            'profile.content_settings.whitelist_setting.adobe-flash-player':1,
            'profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player':1
        }
        options.add_experimental_option('prefs',prefs)
        self.driver=webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get('http://192.168.29.113:8888/login-web/login')
        time.sleep(5)

    def testlogin(self):
        #输入用户名密码
        driver=self.driver
        #页面上某一元素定位超过10秒，则抛出异常
        driver.implicitly_wait(10)

        driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="login-0"]/input[6]').clear()
        driver.find_element_by_xpath('//*[@id="login-0"]/input[6]').send_keys('penglin')
        driver.find_element_by_xpath('//*[@id="password-1"]').clear()
        driver.find_element_by_xpath('//*[@id="password-1"]').send_keys('123')
        driver.find_element_by_xpath('//*[@id="login-0"]/a').click()
        # 选择企业并登录
        driver.find_element_by_xpath('//*[@id="choiceCompany"]/li[3]').click()
        driver.find_element_by_xpath('//*[@id="companyEnter"]').click()
        driver.find_element_by_xpath('//*[@id="choicedSf"]/div[1]').click()

        #进入首页
        time.sleep(5)
        handle=driver.current_window_handle
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/img').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/img').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/img').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/img').click()

        # inputs=driver.find_elements_by_class_name('iknow')
        # if inputs:
        #     for i in inputs:
        #         i.find_element_by_tag_name('img').click()
        #         time.sleep(0.5)
        #         print('点击成功')
        # else:
        #     print("inputs is null")

    def tearDown(self):
        #登录后退出
        time.sleep(20)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()