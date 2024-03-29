from msedge.selenium_tools import Edge
import time

i= 200
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")
driver.get("https://www.amazon.com/-/es/")
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom

    driver.execute_script("window.scrollTo(0, "+str(i)+");")
    i = i+ 200
    # Wait to load page
    time.sleep(1)

    if i >= last_height:
        break

time.sleep(3)

driver.quit()
