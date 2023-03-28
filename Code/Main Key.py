from USB_Security_Key import *
import time
import ctypes
user32 = ctypes.windll.LoadLibrary('user32.dll')
while True:
    if load_config():
        key , filepath = load_config()
        while True:
            try:
                if key == read_from_path(filepath):
                    pass # Correct Key is inputed
                else:
                    user32.LockWorkStation() # Wrong key is inputed
            except:
                user32.LockWorkStation() # No key is inputed

    else:
        show_alert("No config file exists!")
