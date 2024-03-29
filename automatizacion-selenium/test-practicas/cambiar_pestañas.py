#importaciones
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class cambiar_pestañas(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Edge()
    pass

  def test_cambiarPestañas(self):
    driver = self.driver
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    time.sleep(5)
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    time.sleep(5)
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://computer-database.gatling.io/computers")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    pass

  def tearDown(self):

    pass

if __name__ == '__main__':
  unittest.main()