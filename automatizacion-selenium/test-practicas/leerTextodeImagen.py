import cv2
import pytesseract

img = cv2.imread("images.png")
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
texto = pytesseract.image_to_string(img)

print (texto)