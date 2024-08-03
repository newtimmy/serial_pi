import socket
import sys

# Configure the network settings
RPI_IP = 'newtimmys-raspberrypi.local'  # Replace with your Raspberry Pi IP address
# RPI_IP = '192.168.2.2'  # Replace with your Raspberry Pi IP address
RPI_PORT = 12345
MESSAGE = 'Hello, Raspberry Pi!'  # The message to send

try:
    # Set up the network socket
    print(f"Attempting to connect to {RPI_IP}:{RPI_PORT}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(20)  # 10 seconds timeout
    sock.connect((RPI_IP, RPI_PORT))
    print("Connected to the server")

    try:
        # Send the data
        print(f"Sending: {MESSAGE}")
        sock.sendall(MESSAGE.encode())
        # Receive the echo
        echo = sock.recv(1024)
        print(f"Received: {echo.decode()}")
    finally:
        print("Closing socket")
        sock.close()
except socket.timeout:
    print("Connection timed out")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    sys.exit()
