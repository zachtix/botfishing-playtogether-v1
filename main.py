import subprocess
import time
import os
import sys
import pymysql.cursors
from tkinter import * 
from tkinter import messagebox
import tkinter
import printts as tsprint
import keyboard
from printts import tsprint
from funcfishing import first_time_check

# Check HWID
current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
# print(current_machine_id)
clear = lambda: os.system('cls')
clear()

def guide():
    tsprint('วิธีใช้งาน')
    tsprint('กด R เพื่อเริ่ม/รีเซ็ตโปรแกรม')
    tsprint('กด Q เพื่อหยุดโปรแกรม')
    while (True):
        if keyboard.is_pressed("r"):
            tsprint("เริ่มการทำงาน")
            time.sleep(1)
            first_time_check()
        if keyboard.is_pressed("q"):
            tsprint("หยุดโปรแกรม")
            time.sleep(1)
            sys.exit()

try:
    connection = pymysql.connect(host='wcwimj6zu5aaddlj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                user='l9jm464uotxemvah',
                                password='ai0hxuatg2iac0vk',
                                database='lxbh8lw5gf995ay8',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:

        with connection.cursor() as cursor:
            sql = "SELECT `username` FROM `botfishing` WHERE `HWID`=%s"
            cursor.execute(sql, current_machine_id)
            result = cursor.fetchone()
            # print(result)
            if result == None:
                print("Not Have user")
                print('UUID')
                print(current_machine_id)
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("Error", "HWID ไม่ถูกต้อง\nหากต้องการเปลี่ยนเครื่อง\nหรือซื้อ/เช่าโปรแกรม\nกรุณาติดต่อ\nFacebook Page : ZexKODE")
                time.sleep(3600)
            else:
                print("Welcome", result['username'])
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo("Info", "!!!กรุณาอ่าน!!!\nตัวโปรแกรมไม่มีการยุ่งเกี่ยวกับไฟล์เกม\n !!!การใช้โปรแกรมนี้จะไม่รับผิดชอบต่อความเสียหายที่เกิดขึ้น!!! \nหากมีปัญหาการใช้งานกรุณาติดต่อกลับภายใน 2 วัน\nหลังจากซื้อ/เช่า หากแก้ไม่ได้ยินดีคืนเงินเต็มจำนวน\nFacebook Page : ZexKODE")
                guide()

except pymysql.Error:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("Error", "มีปัญหาในการติดต่อกับฐานข้อมูล\nกรุณาติดต่อ\nFacebook Page : ZexKODE")