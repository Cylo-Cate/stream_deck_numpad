import os
import keyboard
import config
from config import keys

solo = True

def ativar_lumi(name):
    if solo:
        os.startfile(r"C:\Users\6364.143\Desktop\Lumi.lnk")

def switch(event):
    global solo
    solo = not solo

keyboard.on_press_key("-", switch, suppress=True)
keyboard.on_press_key("1", lambda e: keys[0]["action"](keys[0]["shortcut"]))

keyboard.wait()
