from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://google.com")
time.sleep(5)

elem1 = driver.find_element(By.LINK_TEXT, "Privacidad")

puntero = ActionChains(driver).move_to_element(elem1)
puntero.perform()

driver.close()