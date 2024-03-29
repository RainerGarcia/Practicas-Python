#importaciones
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import unittest

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Edge()
    self.driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
    pass

  def test_(self):
    driver = self.driver
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='main']/div[3]/div[1]/select")) )
    
    elemento = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/select")
    lista = Select(elemento).options

    for i in lista:
      print(i.text)
      pass

    pass

  def tearDown(self):
    self.driver.close()
    pass

if __name__ == '__main__':
  unittest.main()