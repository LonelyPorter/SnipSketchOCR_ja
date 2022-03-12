import PySimpleGUI as sg
import os
from PIL import ImageGrab
from time import sleep
from ctypes import windll
from easyocr import Reader
from queue import Queue
from threading import Thread
import psutil as ps

def checkProcessRunning(proc_name:str):
    for proc in ps.process_iter():
        if proc_name.lower() in proc.name().lower():
            return True
    return False

def ocr_capture(q:Queue):
    reader = Reader(['ja'], gpu=True)
    while True:
        try:
            text = reader.readtext("paste.png", paragraph=True)
            text = " ".join((t[1] for t in text))
            q.put(text)
            # sleep because the png not get deleted fast enough and will put bunch of text into the queue
            sleep(5)
        except:
            sleep(2)


layout = [  
    [sg.Image(key="-IMAGE-")],
    [[sg.Text(size=(40, 5), key="-TOUT-")], [sg.Button('Copy')]],
    [sg.Button('Capture'), sg.Button('Quit')] 
]

margins=(200, 50)

if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Text Capture', layout, margins=margins)
    text = ""
    q = Queue()
    t1 = Thread(target=ocr_capture, args=(q,))
    t1.setDaemon(True)
    t1.start()

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
                while checkProcessRunning("ScreenClippingHost.exe"):
                    pass
                
                img = ImageGrab.grabclipboard()
                if img:
                    # save the image to be processed
                    img.save('paste.png', 'PNG')

                    # update the image on the window
                    text = q.get()
                    window["-TOUT-"].update(text)
                    window["-IMAGE-"].update(filename='paste.png')

            else:
                print("Fail to open snipping tool")

        elif event == 'Copy':
            print(text)
            sg.clipboard_set(text)
            continue

        if os.path.exists("paste.png"):
            os.remove("paste.png")

    window.close()
