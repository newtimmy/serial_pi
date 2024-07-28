import serial

serial_port = '/dev/pts/4'  # Update to your virtual port
baud_rate = 9600  # Use the same baud rate as configured

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud rate.")
except serial.SerialException as e:
    print(f"Could not open port {serial_port}: {e}")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(f"Received: {line}")