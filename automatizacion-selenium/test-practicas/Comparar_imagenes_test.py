#importaciones
from msedge.selenium_tools import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import unittest
import cv2
import numpy as np
import keyboard

class test_inicio_seccion(unittest.TestCase):
  
  @classmethod
  def setUp(self):
    self.driver = Edge("C:\\driver_edge\\msedgedriver.exe")
    self.driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    time.sleep(10)
    pass

  def test_calculator(self):
    driver = self.driver
    driver.find_element(By.ID, "number1Field").send_keys("2")
    driver.find_element(By.ID, "number2Field").send_keys("2")
    operation = driver.find_element(By.ID, "selectOperationDropdown")
    Select(operation).select_by_value("1")

    driver.find_element(By.ID, "calculateButton").click()
    time.sleep(2)

    driver.save_screenshot("imagen1.png")

    driver.find_element(By.ID, "number1Field").clear()
    driver.find_element(By.ID, "number1Field").send_keys("4")
    driver.find_element(By.ID, "number2Field").clear()
    driver.find_element(By.ID, "number2Field").send_keys("4")
    operation = driver.find_element(By.ID, "selectOperationDropdown")
    Select(operation).select_by_value("2")

    driver.find_element(By.ID, "calculateButton").click()
    time.sleep(2)

    driver.save_screenshot("imagen2.png")
    pass

  def test_comparadorDe2Imagenes(self):
    esperado = cv2.imread("imagen1.png")
    obtenido = cv2.imread("imagen2.png")
    resultado = cv2.subtract(esperado,obtenido)
    if not np.any(resultado):
      print("las imagenes son iguales")
    else:
      print("las imagenes no son iguales")
      """
      #diferencia = cv2.absdiff(img1,img2)
      #imagen_gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)
      contours,_ = cv2.findContours(obtenido,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
      for c in contours:
        posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)
        cv2.rectangle(esperado,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)
        pass

      cv2.imwrite("obtenido.png",obtenido)

      
      while(True):
        cv2.imshow("imagen 1",img1)
        cv2.imshow("imagen 2",img2)
        cv2.imshow("diferencias",diferencia)
        if keyboard.is_pressed("enter"):
          break
          pass
      cv2.destroyAllWindows()
      """
      pass
    pass

  @classmethod
  def tearDown(self):
    self.driver.close()
    pass

if __name__ == '__main__':
  unittest.main()