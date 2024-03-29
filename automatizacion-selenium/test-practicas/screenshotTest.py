#importaciones
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import unittest

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Edge()
    self.driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    time.sleep(10)
    pass

  def test_calculator(self):
    driver = self.driver
    driver.find_element(By.ID, "number1Field").send_keys("5")
    driver.find_element(By.ID, "number2Field").send_keys("6")
    operation = driver.find_element(By.ID, "selectOperationDropdown")
    Select(operation).select_by_value("2")

    driver.find_element(By.ID, "calculateButton").click()
    time.sleep(2)

    print(driver.find_element(By.ID,"numberAnswerField").get_attribute("value"))

    driver.save_screenshot("img1.png")
    pass

  def tearDown(self):
    self.driver.close()
    pass

if __name__ == '__main__':
  unittest.main()