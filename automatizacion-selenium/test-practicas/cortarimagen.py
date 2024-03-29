from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from PIL import Image
from _io import BytesIO

import time

driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("https://www.google.com/")
time.sleep(5)

imagen = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/img")
imagenCompleta = imagen.location
tamaño = imagen.size
captura = driver.get_screenshot_as_png()
imagen2 = Image.open(BytesIO(captura))

left = imagenCompleta["x"]
top = imagenCompleta["y"]
right = imagenCompleta["x"] + tamaño["width"]
bottom = imagenCompleta["y"] + tamaño["height"]

imagen2 = imagen2.crop((left, top, right, bottom))

#imagen2.save("logoYaCortado.png")
imagen2.show()
driver.quit()
