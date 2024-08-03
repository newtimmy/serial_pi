import socket
import serial

# Configure the serial port and network settings
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
SERVER_IP = '0.0.0.0'
SERVER_PORT = 12345

try:
    # Set up the serial connection
    print("Setting up serial connection")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print(f"Serial port {SERIAL_PORT} opened with baud rate {BAUD_RATE}")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

try:
    # Set up the network socket
    print("Setting up network socket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER_IP, SERVER_PORT))
    sock.listen(1)
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
except socket.error as e:
    print(f"Socket error: {e}")
    sys.exit(1)

try:
    print("Waiting for a client to connect...")
    conn, addr = sock.accept()
    print(f"Connected by {addr}")
except Exception as e:
    print(f"Error accepting connection: {e}")
    ser.close()
    sock.close()
    sys.exit(1)

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data}")
        ser.write(data)

        response = ser.read(len(data))
        print(f"Sending: {response}")
        conn.sendall(response)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Closing connections")
    ser.close()
    conn.close()
    sock.close()
