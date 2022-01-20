from PIL import ImageGrab
from easyocr import Reader
from time import sleep
from ctypes import windll
import os


reader = Reader(['ja'], gpu=True)
img = None
print("Starting OCR now:")

# clear clipboard
if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()

while True:
    while not img:
        try:
            img = ImageGrab.grabclipboard()
        except OSError:
            sleep(1)

    img.save('paste.png', 'PNG')

    text = reader.readtext("paste.png", paragraph=True)

    print("Recognized text as follwed:")

    for r in text:
        word = r[1]
        print(word)

    print("\n")

    if os.path.exists("paste.png"):
        os.remove("paste.png")
        
    img = None
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()