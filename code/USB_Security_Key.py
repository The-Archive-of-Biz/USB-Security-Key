def create_login_key():
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=30000))

def create_config(path):
    # Generate random key
    random_key = create_login_key()

    # Write random key and file path to config file
    config = open('config.ini', 'w')
    config.write(f'[DEFAULT]\nRandomKey={random_key}\nFilePath={path}\n')
    config.close()

def load_config():
    # Script to load file path from config file
    try:
        config = open('config.ini', 'r')
        random_key = ''
        file_path = ''
        for line in config:
            if '=' in line:
                split_line = line.split('=')
                if len(split_line) == 2:
                    current_key = split_line[0].strip()
                    current_value = split_line[1].strip()
                    if current_key == 'RandomKey':
                        random_key = current_value
                    elif current_key == 'FilePath':
                        file_path = current_value
        config.close()
        return random_key,file_path
    except:
        return False

def write_to_path(random_key, file_path):
    file = open(f"{file_path}/key.key", 'w')
    file.write(random_key)
    file.close()
    print(f'Random key written to file at {file_path}')
    

def read_from_path(file_path):
    import os
    # Check if key file exists
    key_file_path = os.path.join(file_path, 'key.key')
    if not os.path.exists(key_file_path):
        raise Exception(f'Key file {key_file_path} does not exist')

    # Read key from file
    file = open(key_file_path, 'r')
    random_key = file.read().strip()
    file.close()

    return random_key

def select_file():
    import tkinter as tk
    from tkinter import filedialog
    # Create a Tkinter window and display a folder selector dialog
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def show_alert(message):
    import tkinter as tk
    from tkinter import filedialog
    # Create a Tkinter window and display a message box with the specified message
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showwarning('Alert', message)
