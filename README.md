# ssh connect with your raspberry pi
ssh username@ip_address

# update your linux system and install serial module for python
sudo apt-get update
sudo apt-get install python3-serial

# check for usb devices connected:
ls /dev/ttyUSB*
lsusb

# read data of a given device with the program:
read_serial.py

# use socat to simulate data coming serial port
sudo apt-get update
sudo apt-get install socat

# create sender and receiver
socat -d -d pty,raw,echo=0 pty,raw,echo=0

# send simulated serial communication
echo "Hello, serial port!" > /dev/pts/3

# run event_handler to detect what you are sending
event_handler.py


