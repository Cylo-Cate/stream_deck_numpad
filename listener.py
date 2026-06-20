import os
import keyboard
from config import keys, Numpad_Map

solo = True

def on_press_key(event):
    if event.event_type != "down":
        return
    
    index = Numpad_Map.get(event.scan_code)
    
    key = keys[index]

    if key["action"] is None:
        return

    key["action"](key["shortcut"])


for scan_code in Numpad_Map:
    keyboard.hook_key(scan_code, on_press_key, suppress=True)
    
keyboard.wait('esc')
