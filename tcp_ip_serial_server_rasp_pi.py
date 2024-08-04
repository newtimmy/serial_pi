import socket
import serial
import threading

# Configure the serial port
SERIAL_PORT = '/dev/ttyUSB0'  # Adjust this if needed
SERIAL_BAUDRATE = 9600

# Configure the TCP settings
TCP_IP = '0.0.0.0'
TCP_PORT = 51003

# Function to handle incoming TCP connections
def handle_tcp_client(client_socket, serial_port):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from TCP: {data.decode('utf-8')}")
            serial_port.write(data)
    except Exception as e:
        print(f"TCP connection error: {e}")
    finally:
        client_socket.close()

# Function to handle serial port
def handle_serial(serial_port):
    buffer = ''
    while True:
        if serial_port.in_waiting > 0:
            data = serial_port.read(serial_port.in_waiting).decode('utf-8')
            buffer += data
            if '\n' in buffer:  # Assuming newline as the delimiter
                lines = buffer.split('\n')
                for line in lines[:-1]:
                    print(f"Received from Serial: {line}")
                buffer = lines[-1]

def main():
    # Open the serial port
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    print(f"Serial port {SERIAL_PORT} opened with baud rate {SERIAL_BAUDRATE}")

    # Start thread to handle serial port
    serial_thread = threading.Thread(target=handle_serial, args=(ser,))
    serial_thread.start()

    # Set up the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_IP, TCP_PORT))
    server.listen(5)
    print(f"TCP server listening on {TCP_IP}:{TCP_PORT}")

    try:
        while True:
            client_sock, addr = server.accept()
            print(f"Accepted TCP connection from {addr}")

            # Start a thread to handle the client connection
            client_handler = threading.Thread(
                target=handle_tcp_client,
                args=(client_sock, ser)
            )
            client_handler.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        server.close()
        ser.close()

if __name__ == "__main__":
    main()
