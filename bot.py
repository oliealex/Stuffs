import os
import time
import PIL
import math
import lxml
import requests
#import autopy
import numpy
import datetime
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

character_pos = (637, 460)

char_xbox = 637 - 200
char_ybox = 460 + 400)

Play area = x_pad+1, y_pad +1, 1258, 797
"""

char_xbox = 637
char_ybox = 460
x_pad = 0
y_pad = 96

box_radius = (char_xbox-400, char_ybox-260, char_xbox+400, char_ybox+260)
box_full = (x_pad + 1, y_pad + 1, x_pad + 1258, y_pad + 701)
box_monSign = (1054, 722, 1273, 773)
box_Hp = (11, 129, 206, 147)

cord_monBox = (155,25)
cord_hpBox = (109, 11)
white = (255,255,255,255)
low_Hp = (87,109,96,255)

now = datetime.datetime.now()
laterSec = now.second + 20
laterMin = now.minute + 15


#clicks if monster is detected
"""
def react(box):
    bool = False
    im = screenGrab(box)
    m_color = im.getpixel(cord_monBox)
    if m_color == white:
        bool = True
        pyautogui.click()
    return bool
"""

def new_timer():
    now = datetime.datetime.now()
    laterSec = now.second + 20
    laterMin = now.minute + 15

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

"""
Not finished
def timer():
    now = datetime.datetime.now()
    if now.minute == laterMin:
        new_timer()
        if alertBox() == False:
            exit()
    elif now.second == laterSec:
        new_timer()
        pyautogui.press('2')
"""

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
