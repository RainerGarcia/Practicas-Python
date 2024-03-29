from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
import time 

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://es.javascript.info/alert-prompt-confirm")
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='8vgky3xshl']/div/div[1]/div[1]/a").click()
time.sleep(3)
driver.switch_to.alert.dismiss()

time.sleep(3)

driver.close()