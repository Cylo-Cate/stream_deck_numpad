import os
import keyboard
import config

config.load_page(config.current_page)

def on_press_key(event):
    key = config.keys.get(str(event.scan_code))

    if event.is_keypad != True:
        return
    if event.event_type != "down":
        return
    if key["type"] == None:
        return


    config.Actions[key["type"]](key["shortcut"])


for scan_code in config.keys:
    keyboard.hook_key(int(scan_code), on_press_key, suppress=True)
        

keyboard.wait('esc')
