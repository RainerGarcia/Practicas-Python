#importaciones
from msedge.selenium_tools import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class test_inicio_seccion(unittest.TestCase):

	def setUp(self):

		self.driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
		driver = self.driver
		driver.get("https://demo.guru99.com/test/newtours/")
		driver.maximize_window()
		pass

	def test_login(self):
		#variables a usar
		driver = self.driver
		nombredeusuario = "RSproduct";
		contraseña = "pass1";

		#localizadores
		userlocator = driver.find_element(By.NAME,"userName")
		passlocator = driver.find_element(By.NAME,"password")
		loginlocator = driver.find_element(By.NAME,"submit")

		userlocator.send_keys(nombredeusuario)
		passlocator.send_keys(contraseña)
		loginlocator.click()
		time.sleep(10)
		logintext = driver.find_element(By.XPATH,"//h3[contains(text(),'Login')]").text
		print(logintext)
		pass

	def tearDown(self):
		self.driver.quit()
		pass

if __name__ == '__main__':
	unittest.main()
