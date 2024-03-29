import undetected_edgedriver as ms
from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

usuario = "raineralterno123"
contraseña = "AFK154218"

#driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver = ms.Edge()

driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S101289606%3A1674847039121628&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHdqPiUHAlL8TAe4002UceLx4LwF0qTWaKHxPnFzAotAO2T587eoqbzNTULRlwhmqGWLjTHz")
time.sleep(5)

driver.find_element(By.ID, "identifierId").send_keys(usuario)
driver.find_element(By.ID, "identifierId").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.NAME, "Passwd").send_keys(contraseña)
driver.find_element(By.NAME, "Passwd").send_keys(Keys.ENTER)
time.sleep(3)

texto = driver.find_element(By.TAG_NAME, "h1").text

if text == "Bienvenido, rainer garcia":
	print("-----")
	print("listo")
	print("-----")
	pass

driver.quit()


