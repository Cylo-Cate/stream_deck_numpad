import os
import keyboard
from config import keys

solo = True

def ativar_lumi(name):
    if solo:
        os.startfile(r"C:\Users\6364.143\Desktop\Lumi.lnk")

def switch(event):
    global solo
    solo = not solo

keyboard.on_press_key("-", switch, suppress=True)
keyboard.on_press_key("1", lambda e: keys[0]["action"](keys[0]["shortcut"]), suppress=True)
keyboard.on_press_key("2", lambda e: keys[1]["action"](keys[1]["shortcut"]), suppress=True)
keyboard.on_press_key("3", lambda e: keys[2]["action"](keys[2]["shortcut"]), suppress=True)
keyboard.on_press_key("4", lambda e: keys[3]["action"](keys[3]["shortcut"]), suppress=True)
keyboard.on_press_key("5", lambda e: keys[4]["action"](keys[4]["shortcut"]), suppress=True)


keyboard.wait('esc')
