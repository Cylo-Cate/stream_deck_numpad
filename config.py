import os
import webbrowser
import keyboard

def open_file(file):
    os.startfile(file)
def open_url(site):
    webbrowser.open(site)
def pause_play(_):
    keyboard.send("play/pause media")
def shortcuts(binds):
    keyboard.send(binds)




keys = [
    { #1
        "name": "Lumi",
        "action": open_file,
        "shortcut": r"C:\Users\6364.143\Desktop\Lumi.lnk",
    },
    { #2
        "name": "Gmail",
        "action": open_url,
        "shortcut": "https://mail.google.com/mail/u/0/?ogbl#inbox",
    },
    { #3
        "name": "Play/Pause",
        "action": pause_play,
        "shortcut": "",
    },
     { #4
        "name": "Manager",
        "action": shortcuts,
        "shortcut": "ctrl+shift+esc",
    },
    { #4
        "name": "Mute Discord",
        "action": shortcuts,
        "shortcut": "ctrl+shift+m",
    },
]