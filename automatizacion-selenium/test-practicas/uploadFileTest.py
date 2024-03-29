from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

archivo = "C:\\Users\\raine\\Desktop\\cursos testing software\\automatizacion\\selenium con python\\test_projects\\imagen1.png"
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "input[name='file']").send_keys(archivo)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input.button").click()

texto = driver.find_element(By.ID, "uploaded-files").text

if texto == "imagen1.png":
	print("-----")
	print("listo")
	print("-----")
	pass

