import PySimpleGUI as sg
import os
from PIL import ImageGrab
from time import sleep
from ctypes import windll
from easyocr import Reader

def ocr_capture():
    reader = Reader(['ja'], gpu=True)
    text = reader.readtext("paste.png", paragraph=True)

    return " ".join((t[1] for t in text))

layout = [  
    [sg.Image(key="-IMAGE-")],
    [[sg.Text(size=(40, 1), key="-TOUT-")], [sg.Button('Copy')]],
    [sg.Button('Capture'), sg.Button('Quit')] 
]

margins=(200, 50)

# Create the Window
window = sg.Window('Text Capture', layout, margins=margins)
text = ""

while True:
    event, values = window.read()
     # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Capture':
        # clear clipboard
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()

        img = None
        if os.system('explorer ms-screenclip:'):
            while not img:
                try:
                    img = ImageGrab.grabclipboard()
                except OSError:
                    sleep(1)

            # save the image to be processed
            img.save('paste.png', 'PNG')

            # update the image on the window
            text = ocr_capture()
            window["-TOUT-"].update(text)
            window["-IMAGE-"].update(filename='paste.png')

        else:
            print("Fail to open snipping tool")

    elif event == 'Copy':
        print(text)
        sg.clipboard_set(text)


    if os.path.exists("paste.png"):
        os.remove("paste.png")

window.close()