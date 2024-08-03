import serial

SERIAL_PORT = '/dev/ttyUSB0'  # Adjust according to your setup
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    ser.timeout = 2  # 2 seconds timeout for read
    test_message = b"Hello, loopback!"

    print(f"Sending: {test_message}")
    ser.write(test_message)

    response = ser.read(len(test_message))
    print(f"Received: {response}")

    if test_message == response:
        print("Loopback test passed")
    else:
        print("Loopback test failed")

    ser.close()
except Exception as e:
    print(f"Error: {e}")
