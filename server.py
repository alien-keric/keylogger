import socket

def receive_file(server_address, server_port, save_path):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the server address and port
        server_socket.bind((server_address, server_port))
        
        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening for incoming connections...")
        
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive the file data
        file_data = client_socket.recv(4096)
        
        # Save the received data to a file
        with open(save_path, 'wb') as file:
            file.write(file_data)
        
        print(f"File received and saved to {save_path}")
        
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close the sockets
        client_socket.close()
        server_socket.close()

# Define server address and port
server_address = "0.0.0.0"  # Listen on all available network interfaces
server_port = 4444

# Specify the path to save the received file
save_path = "/tmp/capture.txt"

# Call the function to receive the file
receive_file(server_address, server_port, save_path)

