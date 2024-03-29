from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time
import mouse

options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe",options=options)
busqueda = "sabiondo"
driver.get("https://www.google.com/")
time.sleep(5)
#mouse.move(820, 360)
#mouse.click()
driver.find_element(By.NAME, "q").send_keys(busqueda)
time.sleep(5)
lista = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li/div/div[2]/div[1]/span")

for i in lista:
	
	print(i.text)

driver.close()