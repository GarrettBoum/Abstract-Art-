from tracemalloc import stop
from turtle import onkeypress
import pyautogui
import random
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

if keyboard.press(Key.space): 
    pyautogui.moveTo(1920,1277)

iwidth=random.randint(0,1920)
iheight=random.randint(0,1280)
itime = random.randint(0,10)
pyautogui.moveTo(860,650)

if itime>=10:
    for x in range(2):
        pyautogui.dragTo(iwidth, iheight, duration = 2)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        pyautogui.moveTo(860,650)
        time.sleep(.5)

if itime<=10:
    for x in range(2):
        pyautogui.dragTo(iwidth, iheight, duration = 2)
        pyautogui.moveTo(860,650)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        pyautogui.moveTo(860,650)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        pyautogui.moveTo(860,650)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        pyautogui.moveTo(860,650)
        time.sleep(.5)
        pyautogui.dragTo(iwidth + random.randint(-580,580), iheight + random.randint(-420,420), duration = 1)
        pyautogui.moveTo(860,650)
        time.sleep(.5)

pyautogui.moveTo(816,764)
