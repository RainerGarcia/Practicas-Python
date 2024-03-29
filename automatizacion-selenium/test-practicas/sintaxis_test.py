#importaciones
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Edge()
    self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    self.driver.maximize_window()
    pass

  def test_buscar(self):
    driver = self.driver
    driver.find_element(By.NAME, "keyword").send_keys("fish")
    driver.find_element(By.NAME, "searchProducts").click()
    time.sleep(10)

    texto = driver.find_element(By.XPATH, "//tr[2]/td[3]").text
    self.assertEqual("Goldfish", texto)
    
    assert "no se encontro el elemento:" not in driver.page_source
    
    pass

  def tearDown(self):
    self.driver.close()
    pass

if __name__ == '__main__':
  unittest.main()
