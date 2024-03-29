#importaciones
#import HtmlTestRunner
from msedge.selenium_tools import Edge
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import unittest

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
    self.driver.get("url")
    pass

  def test_(self):
    driver = self.driver
    pass

  def tearDown(self):
    self.driver.quit()
    pass

if __name__ == '__main__':
  #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports/"))
  unittest.main()