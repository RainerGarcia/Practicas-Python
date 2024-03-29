from msedge.selenium_tools import Edge
import time
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://www.google.com/")
time.sleep(6)

cookies = driver.get_cookies()
print()
for i in cookies:
	print(i)
	for j in i:
		print(j)
	print()	

driver.quit()