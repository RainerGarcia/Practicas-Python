from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://jqueryui.com/datepicker/")
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(3)

frame1 = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
driver.switch_to.frame(frame1)

calendar = driver.find_element(By.XPATH, "//*[@id='datepicker']")
calendar.click()

driver.find_element(By.LINK_TEXT, "1").click()

time.sleep(10)
driver.quit()