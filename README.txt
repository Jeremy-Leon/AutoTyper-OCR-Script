About:
This is a Python script that takes an input image of text and types the text for you. Initial motivation was to create a script that could interpret and type paragraphs presented by TypeRacer.com.

NOTE:
  I do not condone using this script to cheat on TypeRacer or anything of the like.
  Over 100 words per minute TypeRacer makes you take an anti-cheat test that this script cannot pass.

This is simply a personal project to get more familiar with Python, OCR, and input listeners. Use at your own risk.


How it works:
This script works by having the user select a region on their display, first by clicking the top left corner of the region and then clicking the lower right corner of the region.

This region is then captured by the program and fed into pytesseract, which produces a string from the image of text. 

This string is then iterated through calling key press functions on each letter of the string, thus typing the selected text for you.


How to use:
Once you run the script, you will run the 'start()' function that takes a float value which represents the interval between charaters you would like.

Example:
	Start(1.0) -> will type a character every 1 second
	Start(0.1) -> will type a character every 1/10th second

The script will then prompt you to press the UP ARROW key to select the region of text you want to be typed. To select the region, you will click on the TOP LEFT corner of the region first, followed by the BOTTOM RIGHT coner of the region. Ensure the region contains all the text and doesn't contain anything it doesn't need to.

The script will then promp you to press the DOWN ARROW key to being the typing, once your cursor is in the appropriate field press the down arrow key.

NOTES:
  Script only works for Windows and Mac (Due to Pillow ImageGrab)

  The selected text region MUST be within the main monitor 
  (Goig outside the main display will result in only a black box as a picture and won't work)


Dependencies:
Tesseract-OCR
Pytesseract
Pynput
Pillow