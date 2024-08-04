import socket
import serial
import threading

# Configure the serial port and TCP settings
SERIAL_PORT = '/dev/ttyUSB0'  # Adjust this if needed
SERIAL_BAUDRATE = 9600
TCP_IP = '0.0.0.0'
TCP_PORT = 51003

# Function to handle incoming TCP connections
def handle_client_connection(client_socket, serial_port):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from TCP: {data}")
            serial_port.write(data)
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

# Main function to set up serial port and TCP server
def main():
    # Open the serial port
    try:
        ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
        print(f"Serial port {SERIAL_PORT} opened with baud rate {SERIAL_BAUDRATE}")
    except Exception as e:
        print(f"Failed to open serial port: {e}")
        return

    # Set up the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((TCP_IP, TCP_PORT))
        server.listen(5)
        print(f"TCP server listening on {TCP_IP}:{TCP_PORT}")
    except Exception as e:
        print(f"Failed to set up TCP server: {e}")
        return

    try:
        while True:
            client_sock, addr = server.accept()
            print(f"Accepted connection from {addr}")

            # Start a thread to handle the client connection
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock, ser)
            )
            client_handler.start()

            # Forward data from the serial port to the TCP client
            while True:
                if ser.in_waiting > 0:
                    data = ser.read(ser.in_waiting)
                    print(f"Received from Serial: {data}")
                    try:
                        client_sock.sendall(data)
                    except Exception as e:
                        print(f"Failed to send data to TCP client: {e}")
                        break
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        server.close()
        ser.close()

if __name__ == "__main__":
    main()
