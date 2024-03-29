from msedge.selenium_tools import Edge
import time
import util
from selenium.webdriver.common.by import By

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
driver.get("https://www.amazon.com/-/es/")
time.sleep(5)

util.fullpage_screenshot(driver,"full.png")
#driver.get_screenshot_as_file("prueba1.png")

#driver.save_screenshot("prueba2.png")

driver.quit()