from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

e = driver.find_element(By.XPATH, "//*[@id='content']/ul/li[1]/a")

e = e.location
t= e.get('x')
i = e.get('y')
print(e)
print(t)
print(i)

driver.quit()