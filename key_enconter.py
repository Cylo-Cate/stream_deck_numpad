import keyboard

def debug(event):
    print("-" * 30)

    for key, value in event.__dict__.items():
        print(f"{key}: {value}")

keyboard.hook(debug)
keyboard.wait("esc")