import socket
import sys

# RPI_IP = '192.168.178.56'
RPI_IP = '192.168.178.10'
RPI_PORT = 12345
MESSAGE = 'Hello, Raspberry Pi!'

try:
    print(f"Attempting to connect to {RPI_IP}:{RPI_PORT}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((RPI_IP, RPI_PORT))
    print("Connected to the server")

    try:
        print(f"Sending: {MESSAGE}")
        sock.sendall(MESSAGE.encode())
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
