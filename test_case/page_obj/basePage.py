#conding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

class page(object):
    def _open(self):
        pass
    def open(self):
        pass

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    