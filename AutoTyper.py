from PIL import Image, ImageGrab, ImageOps
import pytesseract
import time
import datetime
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.keyboard import Key, Controller

keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

class OCR:

    clickCount = 0
    pCords = [0,0,0,0]
    defined = False
    pImage = None
    
    def areaSelect():
        
        print('Click twice to define TEXT window')
            
        def on_click(x, y, button, pressed):
            
            if pressed:
                print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
                if OCR.clickCount == 0:
                    OCR.pCords[0] = x
                    OCR.pCords[1] = y
                elif OCR.clickCount == 1:
                    OCR.pCords[2] = x
                    OCR.pCords[3] = y
                    OCR.defined = True
                    print('')
                    OCR.clickCount = 0
                    return False
                OCR.clickCount += 1
                
        with ms.Listener(on_click = on_click) as listener:
            listener.join()

    def keyPress():

        print('Press UP ARROW to select OCR region')
        
        def on_press(key):
            i = 10

        def on_release(key):
            if key == Key.esc:
                print('Stopping key listener')
                return False
            elif key == Key.up:
                print('UP arrow pressed\n')
                OCR.areaSelect()
                OCR.capture()
                
                return False

        with kb.Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()

    def startTyping(delayTime: float):

        print('Press DOWN ARROW to start typing')
        
        def on_press(key):
            i = 10

        def on_release(key):
            if key == Key.esc:
                print('Stopping key listener')
                return False
            elif key == Key.down:
                print('DOWN arrow pressed\n')
                OCR.output(delayTime)
                return False

        with kb.Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()


    def capture():
        
        if OCR.defined:
            OCR.pImage = ImageGrab.grab(bbox = (OCR.pCords[0],OCR.pCords[1],OCR.pCords[2],OCR.pCords[3]))
        else:
            print('please define an area to OCR before trying to print')
            
    def output(delayTime: float):
            
            paraString = pytesseract.image_to_string(OCR.pImage)
            length = len(paraString)
            paraString = paraString.replace('|','I')
            paraString = paraString.replace('\n',' ')
  
            for i in range(length):
                keyboard.press(paraString[i])
                keyboard.release(paraString[i])
                time.sleep(delayTime)
                    
            print('The Processed String:\n',paraString,'\n')

       
def start(delayTime: float):
    
    print('Time interal between chars:',delayTime)
    OCR.keyPress()
    OCR.startTyping(delayTime)
    



