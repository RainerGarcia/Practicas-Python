#importaciones
#import HtmlTestRunner
from msedge.selenium_tools import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
    self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    self.driver.maximize_window()
    pass

  def test_buscar(self):
    driver = self.driver
    driver.find_element(By.NAME, "keyword").send_keys("fish")
    driver.find_element(By.NAME, "searchProducts").click()
    time.sleep(10)

    texto = driver.find_element(By.XPATH, "//tr[2]/td[3]").text
    
    #se puede usar este, solo con dos parámetros
    #self.assertEqual("Goldfish", texto, "error no es igual")

    #y este se usa con un tercer parámetro para decir un
    #mensaje de error o fail
    self.assertEqual("Goldfish", texto, "error no es igual")   
    pass

  def tearDown(self):
    self.driver.quit()
    pass

if __name__ == '__main__':
  #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports/"))
  unittest.main()