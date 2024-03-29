from msedge.selenium_tools import Edge
import time
from selenium.webdriver.common.by import By

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://www.google.com/")

driver.find_element(By.CLASS_NAME, "gb_e").click()
time.sleep(4)
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[name='app']"))
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[12]/a/div/span").click()
time.sleep(4)

driver.quit()