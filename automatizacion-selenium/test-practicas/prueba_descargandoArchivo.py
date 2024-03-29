from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\\Users\\raine\\Desktop\\cursos testing software\\automatizacion\\selenium con python\\test_projects\\reports"
})
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe", options=options)


driver.get("https://the-internet.herokuapp.com/download")
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Crazy.jpg")))

driver.find_element(By.LINK_TEXT, "Crazy.jpg").click()
time.sleep(5)

driver.quit()