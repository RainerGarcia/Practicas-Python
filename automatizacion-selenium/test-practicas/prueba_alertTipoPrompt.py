from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
import time 

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://es.javascript.info/alert-prompt-confirm")
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='b61m60oj36']/div/div[1]/div[1]/a").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.send_keys("29")
time.sleep(3)
alert.accept()
time.sleep(3)
print(driver.switch_to.alert.text)
time.sleep(3)
alert.dismiss()
time.sleep(3)
driver.quit()