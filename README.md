# SnipSketchOCR_ja  
![Visitors](https://visitor-badge.glitch.me/badge?page_id=LonelyPorter/SnipSketchOCR_ja)  

A text recognition tool (OCR) to capture text (Japanese) on screenshot taken by Snip & Sketch (Windows tool)
It will save the picture on the clipboard on disk and do the text recognition.

## Requirement
* Python 3.6+
* Pacakges:
  * PyTorch
  * easyocr
  * PySimpleGUI (if GUI is wanted)
  * (more on requirements.txt)


## Installation
```
py -m pip install -r requirements.txt
```  
This will install PyTorch 11.3 with CUDA support and easyocr, plus other packages that needed. (OpenCV, Pillow...)

## Usage
* Command Line 
  * Start the program either double click at `main.py` or run with python `python main.py`
  * It will take time to load the model but you will see `Starting OCR now:` as it begins to take input
  * After it starts, take a screenshot of some text (Japanese) with windows' Snip & Sketch tool or any screenshot tool (as long as it copies the screenshot into the clipboard).
  Then, the recognized text will be showed on the next line on the output screen.
  * The application will keep on running and wait for you take a screenshot. You can close it by hitting the close button or type in  
  `Ctrl + c`
* GUI
  * run on cmd : ```py ssocr.py``` or double click to launch on windows (under the folder where all the requirement packages are installed)
  * Hit `Capture` to start the snipping tool and capture a picture for text recognition  
    Hit `Copy` after "Capture" to copy the recognized text to clipboard
  * (more update soon...)

## Note
It is not guaranteed to recognize the text 100% correct!

## References
[PyTorch](https://pytorch.org/)  
[GitHub: EasyOCR](https://github.com/JaidedAI/EasyOCR)  
[轻松识别图像，这款Python OCR库支持超过80种语言](https://zhuanlan.zhihu.com/p/342686109)  
[PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
