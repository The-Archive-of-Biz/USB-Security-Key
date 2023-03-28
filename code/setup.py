from USB_Security_Key import *

try:
    show_alert("Please select the file location of your USB.")
    create_config(select_file())
    key , filepath = load_config()
    write_to_path(key, filepath)
    show_alert("Setup Succesful.")
except:
    show_alert("An error has occured!")
