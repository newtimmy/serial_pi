import serial
import time

# Use the default serial port
serial_port = '/dev/serial0'
baud_rate = 9600
output_file = 'serial_data.txt'

try:
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud")

    # Open the file in append mode
    with open(output_file, 'a') as f:
        while True:
            if ser.in_waiting > 0:
                # Read the data from the serial port
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Received: {data}")

                # Write the data to the file
                f.write(f"{data}\n")
                f.flush()  # Ensure the data is written to the file immediately
            time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("Exiting program")

finally:
    # Close the serial port if it is open
    if ser.is_open:
        ser.close()
