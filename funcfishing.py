__author__ = 'ZexKODE'

import os
import sys
import subprocess
import pymysql.cursors
import cv2 as cv
# import numpy as np
from windowcapture import WindowCapture
# from pynput.keyboard import Key, Controller
# keyboard = Controller() 
import keyboard
# import win32gui, win32con, win32api
from time import sleep
from printts import tsprint
from datetime import datetime
import pytz
from tkinter import * 
from tkinter import messagebox
import tkinter
import ast
os.chdir(os.path.dirname(os.path.abspath(__file__)))

current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

window = 'botfishing'

needle_img = cv.imread('alert.jpg', cv.IMREAD_UNCHANGED)
collect_img = cv.imread('collect.jpg', cv.IMREAD_UNCHANGED)

count_collect = 0

def detect_fish():
    wincap = WindowCapture(window)
    keyboard.press_and_release('z')
    tsprint('Find Fish.')
    # sleep(1)
    while(True):
        screenshot = wincap.get_screenshot()
        result = cv.matchTemplate(screenshot, needle_img, cv.TM_CCOEFF_NORMED)
        # result = cv.matchTemplate(screenshot, needle_img)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        threshold = 0.8
        if max_val >= threshold:
            tsprint('Found Fish.')
            keyboard.press_and_release('e')
            sleep(0.5)
            if keyboard.is_pressed("r"):
                tsprint("รีเซ็ตการทำงาน")
                sleep(1)
                detect_time()
            if keyboard.is_pressed("q"):
                tsprint("หยุดโปรแกรม")
                sleep(1)
                sys.exit()
            while(True):
                # win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, 0x45, 0)
                # sleep(0.1)
                # win32api.PostMessage(hwndMain, win32con.WM_KEYUP, 0x45, 0)
                detect_collect()
        # while (True):
        if keyboard.is_pressed("r"):
            tsprint("รีเซ็ตการทำงาน")
            sleep(1)
            detect_time()
        if keyboard.is_pressed("q"):
            tsprint("หยุดโปรแกรม")
            sleep(1)
            sys.exit()


def detect_collect():
    sleep(1)
    wincap = WindowCapture(window)
    collect_img = cv.imread('collect.jpg', cv.IMREAD_UNCHANGED)
    tsprint('Find Collect.')
    while(True):
        screenshot = wincap.get_screenshot()
        result = cv.matchTemplate(screenshot, collect_img, cv.TM_CCOEFF_NORMED)
        # result = cv.matchTemplate(screenshot, collect_img)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        threshold = 0.5
        if max_val >= threshold:
            keyboard.press_and_release('x')
            global count_collect
            count_collect = count_collect+1
            s = 'Collect : '
            ss = s+str(count_collect)
            tsprint(ss) 
            sleep(2)
            detect_fish()
        # while (True):
        if keyboard.is_pressed("r"):
            tsprint("รีเซ็ตการทำงาน")
            sleep(1)
            detect_time()
        if keyboard.is_pressed("q"):
            tsprint("หยุดโปรแกรม")
            sleep(1)
            sys.exit()



def detect_time():
    # while(True):
    try:
        connection = pymysql.connect(host='wcwimj6zu5aaddlj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                    user='l9jm464uotxemvah',
                                    password='ai0hxuatg2iac0vk',
                                    database='lxbh8lw5gf995ay8',
                                    cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                queryexp = "SELECT `EXP` FROM `botfishing` WHERE `HWID`=%s"
                cursor.execute(queryexp, current_machine_id)
                resultexp = cursor.fetchone()
                EXP = resultexp['EXP']
                D2=ast.literal_eval(EXP) ## Chang Class Str to Dict
                year = int(D2["Year"])
                month = int(D2["Month"])
                day = int(D2["Day"])
                hours = int(D2["Hours"])
                tz_TH = pytz.timezone('Asia/Bangkok')
                datetime_TH = datetime.now(tz_TH)
                cms = int(datetime_TH.strftime("%M"))
                if cms == 1:
                    tz_TH = pytz.timezone('Asia/Bangkok')
                    datetime_TH = datetime.now(tz_TH)
                    CYear = int(datetime_TH.strftime("%Y"))
                    CMonth = int(datetime_TH.strftime("%m"))
                    CDay = int(datetime_TH.strftime("%d"))
                    CHours = int(datetime_TH.strftime("%H"))
                    if year > CYear:
                        tsprint('Check Time : Pass')
                        detect_fish()
                    else:
                        if month > CMonth:
                            tsprint('Check Time : Pass')
                            detect_fish()
                        else:
                            if day > CDay:
                                tsprint('Check Time : Pass')
                                detect_fish()
                            else:
                                if hours > CHours:
                                    tsprint('Check Time : Pass')
                                    detect_fish()
                                else:
                                    root = tkinter.Tk()
                                    root.withdraw()
                                    messagebox.showerror("Error", "โปรแกรมคุณหมดอายุ\nหากต้องการเช่าต่อ ติดต่อ\nFacebook Page : ZexKODE")
                                    sys.exit()
                else:
                    detect_fish()
    except pymysql.Error:
        tsprint('error')
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("Error", "มีปัญหาในการติดต่อกับฐานข้อมูล\nกรุณาติดต่อ\nFacebook Page : ZexKODE")
        
# detect_time()

def first_time_check():
    try:
        connection = pymysql.connect(host='wcwimj6zu5aaddlj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                    user='l9jm464uotxemvah',
                                    password='ai0hxuatg2iac0vk',
                                    database='lxbh8lw5gf995ay8',
                                    cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                queryexp = "SELECT `EXP` FROM `botfishing` WHERE `HWID`=%s"
                cursor.execute(queryexp, current_machine_id)
                resultexp = cursor.fetchone()
                EXP = resultexp['EXP']
                D2=ast.literal_eval(EXP) ## Chang Class Str to Dict
                year = int(D2["Year"])
                month = int(D2["Month"])
                day = int(D2["Day"])
                hours = int(D2["Hours"])
                tz_TH = pytz.timezone('Asia/Bangkok')
                datetime_TH = datetime.now(tz_TH)
                # cms = int(datetime_TH.strftime("%M"))
                # if cms == 1:
                tz_TH = pytz.timezone('Asia/Bangkok')
                datetime_TH = datetime.now(tz_TH)
                CYear = int(datetime_TH.strftime("%Y"))
                CMonth = int(datetime_TH.strftime("%m"))
                CDay = int(datetime_TH.strftime("%d"))
                CHours = int(datetime_TH.strftime("%H"))
                if year > CYear:
                    tsprint('Check Time : Pass')
                    detect_fish()
                else:
                    if month > CMonth:
                        tsprint('Check Time : Pass')
                        detect_fish()
                    else:
                        if day > CDay:
                            tsprint('Check Time : Pass')
                            detect_fish()
                        else:
                            if hours > CHours:
                                tsprint('Check Time : Pass')
                                detect_fish()
                            else:
                                root = tkinter.Tk()
                                root.withdraw()
                                messagebox.showerror("Error", "โปรแกรมคุณหมดอายุ\nหากต้องการเช่าต่อ ติดต่อ\nFacebook Page : ZexKODE")
                                sys.exit()
                # else:
                #     detect_fish()
    except pymysql.Error:
        tsprint('error')
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("Error", "มีปัญหาในการติดต่อกับฐานข้อมูล\nกรุณาติดต่อ\nFacebook Page : ZexKODE")

# first_time_check()