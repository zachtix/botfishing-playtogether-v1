import sys
import cv2 as cv
from windowcapture import WindowCapture
import keyboard
from time import sleep

window = 'botfishing'

needle_img = cv.imread('alert.jpg', cv.IMREAD_UNCHANGED)
collect_img = cv.imread('collect.jpg', cv.IMREAD_UNCHANGED)

count_collect = 0

def detect_fish():
    wincap = WindowCapture(window)
    keyboard.press_and_release('z')
    print('Find Fish.')
    while(True):
        screenshot = wincap.get_screenshot()
        result = cv.matchTemplate(screenshot, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        threshold = 0.8
        if max_val >= threshold:
            print('Found Fish.')
            keyboard.press_and_release('e')
            sleep(0.5)
            if keyboard.is_pressed("r"):
                print("รีเซ็ตการทำงาน")
                sleep(1)
                detect_fish()
            if keyboard.is_pressed("q"):
                print("หยุดโปรแกรม")
                sleep(1)
                sys.exit()
            while(True):
                detect_collect()
        if keyboard.is_pressed("r"):
            print("รีเซ็ตการทำงาน")
            sleep(1)
            detect_fish()
        if keyboard.is_pressed("q"):
            print("หยุดโปรแกรม")
            sleep(1)
            sys.exit()


def detect_collect():
    sleep(1)
    wincap = WindowCapture(window)
    collect_img = cv.imread('collect.jpg', cv.IMREAD_UNCHANGED)
    print('Find Collect.')
    while(True):
        screenshot = wincap.get_screenshot()
        result = cv.matchTemplate(screenshot, collect_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        threshold = 0.5
        if max_val >= threshold:
            keyboard.press_and_release('x')
            global count_collect
            count_collect = count_collect+1
            s = 'Collect : '
            ss = s+str(count_collect)
            print(ss) 
            sleep(2)
            detect_fish()
        if keyboard.is_pressed("r"):
            print("รีเซ็ตการทำงาน")
            sleep(1)
            detect_fish()
        if keyboard.is_pressed("q"):
            print("หยุดโปรแกรม")
            sleep(1)
            sys.exit()