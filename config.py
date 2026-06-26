import os
import webbrowser
import keyboard
import json
import pyautogui

current_page = 1

def open_file(file):
    os.startfile(file)
def open_url(site):
    webbrowser.open(site)
def pause_play(_):
    keyboard.send("play/pause media")
def shortcut(binds):
    keyboard.send(binds)
def write_text(text):
    pyautogui.typewrite(text) 
def pages_switch(_):
    global current_page
    current_page += 1
    if current_page > total_pages:
        current_page = 1
    load_page(current_page)



Actions = {
    "url": open_url,
    "program": open_file,
    "hotkey": shortcut,
    "pause_play": pause_play,
    "switch_pages": pages_switch,
    "text": write_text,
}
total_pages = len([
    file for file in os.listdir("pages")
    if file.startswith("page") and file.endswith(".json")
])


def load_page(page):
    global keys

    with open(f"pages/page{page}.json", "r", encoding="utf-8") as f:
        keys = json.load(f)



