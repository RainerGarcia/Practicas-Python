from msedge.selenium_tools import Edge
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://react-bootstrap-v4.netlify.app/#")

time.sleep(5)

versionlocator = driver.find_element(By.ID, "dropdown-version")
getlocator = driver.find_element(By.LINK_TEXT, "Get started")

puntero = ActionChains(driver)

puntero.double_click(versionlocator)
puntero.pause(3)
puntero.context_click(getlocator)
puntero.pause(3)
puntero.perform()

driver.quit()
