from PIL import Image, ImageGrab, ImageOps
import pytesseract
import time
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.keyboard import Key, Controller

keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

class AutoTyper:
    
    clickCount = 0
    pCords = [0,0,0,0]
    defined = False
    pImage = None
    
    def areaSelect():
        
        print('Click twice to define TEXT window')
            
        def on_click(x, y, button, pressed):
            
            if pressed:
                print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
                if AutoTyper.clickCount == 0:
                    AutoTyper.pCords[0] = x
                    AutoTyper.pCords[1] = y
                elif AutoTyper.clickCount == 1:
                    AutoTyper.pCords[2] = x
                    AutoTyper.pCords[3] = y
                    AutoTyper.defined = True
                    print('')
                    AutoTyper.clickCount = 0
                    return False
                AutoTyper.clickCount += 1
                
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
                AutoTyper.areaSelect()
                AutoTyper.capture()
                
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
                AutoTyper.output(delayTime)
                return False

        with kb.Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()


    def capture():
        
        if AutoTyper.defined:
            AutoTyper.pImage = ImageGrab.grab(bbox = (AutoTyper.pCords[0],AutoTyper.pCords[1],AutoTyper.pCords[2],AutoTyper.pCords[3]))
        else:
            print('please define an area to OCR before trying to print')
            
    def output(delayTime: float):
            
            paraString = pytesseract.image_to_string(AutoTyper.pImage)
            length = len(paraString)

            # Character replacement to make outpur more accurate
            paraString = paraString.replace('|','I')
            paraString = paraString.replace('\n',' ')
  
            for i in range(length):
                keyboard.press(paraString[i])
                keyboard.release(paraString[i])
                time.sleep(delayTime)
                    
            print('The Processed String:\n',paraString,'\n')

       
def start(delayTime: float):
    
    print('Time interal between chars:',delayTime)
    AutoTyper.keyPress()
    AutoTyper.startTyping(delayTime)
    



