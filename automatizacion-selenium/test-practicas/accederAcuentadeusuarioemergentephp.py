from msedge.selenium_tools import Edge
import keyboard
import pyautogui
import time
driver = Edge(executable_path="C:\\driver_edge\\msedgedriver.exe")

driver.get("http://217.182.87.241/testlink/login.php")
time.sleep(3)

keyboard.write("usuario")
time.sleep(3)
pyautogui.press("tab")
keyboard.write("contraseña")
time.sleep(3)
pyautogui.press("Enter")
time.sleep(3)
driver.quit()