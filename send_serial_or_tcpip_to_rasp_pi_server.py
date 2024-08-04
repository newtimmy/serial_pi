import socket
import serial
import time

def send_data_via_serial(com_port, baudrate, data):
    try:
        ser = serial.Serial(com_port, baudrate, timeout=1)
        ser.write(data.encode('utf-8'))
        time.sleep(1)  # Give it some time to process and loop back the data
        response = ser.read(ser.in_waiting).decode('utf-8')
        ser.close()
        print(f"Received from serial: {response}")
    except Exception as e:
        print(f"Error: {e}")

def send_data_via_ip(ip, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(data.encode('utf-8'))
            response = s.recv(1024).decode('utf-8')
            print(f"Received from IP: {response}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    mode = input("Choose mode (serial/ip): ").strip().lower()
    data_to_send = input("Enter the data to send: ").strip()

    if mode == 'serial':
        com_port = input("Enter COM port (e.g., COM5): ").strip()
        baudrate = int(input("Enter baud rate (e.g., 9600): ").strip())
        send_data_via_serial(com_port, baudrate, data_to_send)
    elif mode == 'ip':
        ip_address = input("Enter IP address (e.g., 192.168.1.100): ").strip()
        port = int(input("Enter port (e.g., 51003): ").strip())
        send_data_via_ip(ip_address, port, data_to_send)
    else:
        print("Invalid mode. Please choose either 'serial' or 'ip'.")

if __name__ == "__main__":
    main()
