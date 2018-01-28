import os
import time
import PIL
from PIL import Image
from PIL import ImageGrab

"""
All coordinates assume a screen resolution of 1280x800, and Chrome
maximized with the Bookmakrs Toolbar enabled.
x_pad = 0
y_pad = 96

character_pos = (637, 460)

char_xbox = 637 - 200
char_ybox = 460 + 400)

Play area = x_pad+1, y_pad +1, 1258, 797
"""
char_xbox = 637
char_ybox = 460


x_pad = 0
y_pad = 96


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1258, y_pad + 701)
    image = PIL.ImageGrab.grab(bbox=None)
    image.save(os.getcwd() + '//full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screenGrab()

if __name__ == '__main__':
    main()
