#importaciones
from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
#from selenium.webdriver.support.ui import Select 
from selenium.webdriver import ActionChains

class test_inicio_seccion(unittest.TestCase):

  def setUp(self):
    self.driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
    self.driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
    time.sleep(10)
    pass

  def test_move_puntero(self):
    driver = self.driver
    mouse = ActionChains(driver)
    botones = driver.find_elements(By.CSS_SELECTOR, "div.slider")
    
    for i in botones:
      mouse.move_to_element(i).click()
      time.sleep(1)
      pass

    mouse.perform()

    time.sleep(5)
    
    mouse.reset_actions()
    mouse = ActionChains(driver)
    mouse.move_to_element(driver.find_element(By.ID, "navbtn_tutorials")).click()
    mouse.perform()
    
    time.sleep(3)

    mouse.reset_actions()
    mouse = ActionChains(driver)
    mouse.move_to_element(driver.find_element(By.LINK_TEXT, "Learn Python")).click()
    mouse.perform()
    
    mouse.reset_actions()

    time.sleep(10)
    
    texto = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/p[1]").text

    self.assertEqual("Python is a popular programming language.",texto)

    pass
  def tearDown(self):
    self.driver.quit()
    pass

if __name__ == '__main__':
  unittest.main()