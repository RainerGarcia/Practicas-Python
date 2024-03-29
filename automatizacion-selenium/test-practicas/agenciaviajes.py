from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pyautogui

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://www.bestday.com.mx/ofertas-viajes/puente-febrero#mo")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='lgpd-banner']/div/a[2]").click()
driver.maximize_window()
driver.execute_script("document.body.style.zoom='80%'")
time.sleep(3)
"""
driver.find_element(By.XPATH, "//*[@id='searchbox-v2']/div/div/div/div/div/div[3]/div[1]/div/div[1]/div[1]/div/input").send_keys("Valencia, Carabobo, Venezuela")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='searchbox-v2']/div/div/div/div/div/div[3]/div[1]/div/div[2]/div/div/input").send_keys("Ciudad de México, México D.F., México")
time.sleep(3)
"""


calendar = driver.find_element(By.XPATH, "//*[@id='searchbox-v2']/div/div/div/div/div/div[3]/div[2]/div[1]")
e = calendar.location
x = e.get('x')
y = e.get('y')
pyautogui.moveTo(x,y)
pyautogui.click()

#pyautogui.moveTo(calendar)
#pyautogui.click()

#driver.find_element(By.XPATH,"//*[@id='component-modals']/div[1]/div[1]/div[2]/div[1]/div[3]/div[4]/div").click()

#driver.find_element(By.XPATH,"//*[@id='component-modals']/div[1]/div[1]/div[2]/div[1]/div[3]/div[25]/div").click()
"""
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='component-modals']/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[11]/div").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='component-modals']/div[1]/div[3]/div/div[2]/button/em").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='searchbox-v2']/div/div/div/div/div/div[3]/div[3]/div/div/div/div[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='svg-plus-uJ24xqk']").click()
driver.find_element(By.XPATH,"//*[@id='svg-plus-uJ24xqk']").click()
time.sleep(3)
suma = driver.find_elements(By.XPATH,"//*[@id='svg-plus-uJ24xqk']")
suma[0].click()
suma[0].click()
suma[1].click()
time.sleep(3)
edad = driver.find_elements(By.XPATH,"//*[@id='component-modals']/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/select")
edad[11].click()
time.sleep(3)
driver.find_element(By.XPATH,"")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='component-modals']/div[2]/div[3]/div/a[1]/em").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='searchbox-v2']/div/div/div/div/div/div[3]/div[4]/button")
time.sleep(10)

driver.save_screenshot("viajes.png")
time.sleep(3)
"""

time.sleep(10)
driver.quit()



