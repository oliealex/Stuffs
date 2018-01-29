import os
import time
import PIL
import math
import lxml
import requests
#import autopy
import numpy
import pyautogui
#-----------------------
from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps
#from autopy import alert
from numpy import *
from lxml import html


"""
Assuming you are playing on a 24' screen
x_pad = 0
y_pad = 96

char_xbox = 637 - 200
char_ybox = 460 + 400)

Play area = x_pad+1, y_pad +1, 1258, 797
"""
page = requests.get('http://hordes.io/#')
tree = html.fromstring(page.content)

box_full = (x_pad + 1, y_pad + 1, x_pad + 1258, y_pad + 701)
box_Hp = (11, 129, 206, 147)

cord_hpBox = (109, 11)
low_Hp = (87,109,96,255)

def

def init():
    pyautogui.press('2')

def heal():
    im = screenGrab(box_Hp)
    m_color = im.getpixel(cord_hpBox)
    if m_color == low_Hp:
        pyautogui.press('1')


#not finished
def alertBox():
    bool = True
    if alert.alert("Do you want the bot to start/continue press OK", cancel_button="cancel") == False:
        bool = False
    return bool

def attack():
    pyautogui.press('tab')
    pyautogui.press('3')


def screenGrab(box):
    image = PIL.ImageGrab.grab(bbox=box)
    #image.save(os.getcwd() + '//full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return image

def main():
    init()
    i = 0
    while True:
        heal()
        attack()
        i = i + 1
        time.sleep(1)
        if i == 15:
            i = 0
            pyautogui.press('2')

if __name__ == '__main__':
    main()
