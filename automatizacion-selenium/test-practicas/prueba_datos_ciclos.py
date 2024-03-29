from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
import time

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://testsheepnz.github.io/BasicCalculator.html")
time.sleep(5)
firstNumber = driver.find_element(By.NAME, "number1")
secondNumber = driver.find_element(By.NAME, "number2")
operation = operation = driver.find_elements(By.XPATH, "//*[@id='selectOperationDropdown']/option")
calculate = driver.find_element(By.ID, "calculateButton")
result = driver.find_element(By.NAME, "numberAnswer")

with open("operaciones.txt") as file:
	lineas = file.readlines()
	for i in lineas:
		datos = i.split(",")
		
		firstNumber.clear()
		firstNumber.send_keys(str(datos[0]))
		secondNumber.clear()
		secondNumber.send_keys(str(datos[1]))
		operation[int(datos[2])].click()
		time.sleep(2)
		calculate.click()
		time.sleep(2)
		print(result.get_attribute("value"))

file.close()
driver.quit()
