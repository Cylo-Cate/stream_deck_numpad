import os
import keyboard
from config import keys, Numpad_Map

solo = True

def switch(event):
    global solo
    solo = not solo

def on_press_key(event):
    if event.is_keypad != True:
        return
    if event.event_type != "down":
        return
    
    index = Numpad_Map.get(event.scan_code)
    
    key = keys[index]

    if key["action"] is None:
        return

    key["action"](key["shortcut"])

if solo != False:
    for scan_code in Numpad_Map:
        keyboard.hook_key(scan_code, on_press_key, suppress=True)
        
else:
    keyboard.on_press_key("num lock", switch)
keyboard.wait('esc')
