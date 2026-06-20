import os
import keyboard
from config import keys, Numpad_Map

solo = True

def on_press_key(event):
    if event.event_type != "down":
        return
    
    index = Numpad_Map.get(event.scan_code)
    
    if index != None:
        keys[index]["action"](keys[index]["shortcut"])

# def switch(event):
#     global solo
#     solo = not solo

keyboard.hook(on_press_key)
keyboard.wait('esc')
