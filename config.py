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
    
Numpad_Map = {
    69: 0,   # NumLock
    53: 1,   # /
    55: 2,   # *
    74: 3,   # -
    71: 4,   # 7
    72: 5,   # 8
    73: 6,   # 9
    78: 7,   # +
    75: 8,   # 4
    76: 9,   # 5
    77: 10,  # 6
    79: 11,  # 1
    80: 12,  # 2
    81: 13,  # 3
    82: 14,  # 0
    126: 15, # .
    28: 16,  # Enter
}




keys = [
    { #NumLock
        "name": "Lumi",
        "action": open_file,
        "shortcut": r"C:\Users\6364.143\Desktop\Lumi.lnk",
    },
    { #/
        "name": "Gmail",
        "action": open_url,
        "shortcut": "https://mail.google.com/mail/u/0/?ogbl#inbox",
    },
    { #*
        "name": "Play/Pause",
        "action": pause_play,
        "shortcut": None,
    },
    { #-
        "name": "Manager",
        "action": shortcuts,
        "shortcut": "ctrl+shift+esc",
    },
    { #7
        "name": "Mute Discord",
        "action": shortcuts,
        "shortcut": "ctrl+shift+m",
    },
    { #8
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #9
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #+
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #4
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #5
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #6
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #1
        "name": "A",
        "action": open_url,
        "shortcut": "www.youtube.com",
    },
    { #2
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #3
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #Enter
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #0
        "name": None,
        "action": None,
        "shortcut": None,
    },
    { #.
        "name": None,
        "action": None,
        "shortcut": None,
    },
]