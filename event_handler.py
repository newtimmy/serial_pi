import serial
import time
import subprocess

# Configure the serial port and baud rate.
# Replace '/dev/ttyUSB0' with your serial port name.
serial_port = '/dev/pts/1'
baud_rate = 9600

# Initialize the serial connection.
ser = serial.Serial(serial_port, baud_rate, timeout=1)


def handle_event():
    # Define what to do when the event is triggered.
    print("Event detected!")
    subprocess.call(['bash',"play_sound.sh"], cwd="/home/timm")



def main():
    try:
        while True:
            # Read data from the serial port.
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()

                # Check if the data matches your condition.
                if data.find("Hello data"):
                    handle_event()

            # Sleep for a short period to avoid busy-waiting.
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        ser.close()


if __name__ == '__main__':
    main()
