import serial
import time

# Adjust this to the correct virtual serial port
serial_port = '/dev/pts/3'
baud_rate = 9600

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud")

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")
        time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("Exiting program")

finally:
    if ser.is_open:
        ser.close()