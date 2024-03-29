#importaciones
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class cambioPaginaAnteriorSiguiente(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Edge()
    self.driver.get("https://myprofitland.com/")
    time.sleep(5)
    pass

  def test_pagina_siguiente_anterior(self):
    driver = self.driver
    driver.find_element(By.CLASS_NAME, "topnav-toggle").click()
    time.sleep(2)
    #driver.find_element(By.XPATH, "//*[@id='topnav-collapse']/ul/li[2]/a").click()
    #time.sleep(5)
    #driver.find_element(By.CLASS_NAME, "topnav-toggle").click()
    #time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='topnav-collapse']/ul/li[4]/a").click()
    #time.sleep(5)
    #driver.back()
    #time.sleep(5)
    #driver.forward()
    #time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Home Page").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//font[contains(text(), 'Starting Page')]").is_displayed()
    pass

  def tearDown(self):

    pass

if __name__ == '__main__':
  unittest.main()