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

# download data from raspberry pi
scp -P port_number -r pi@192.168.1.100:/home/pi/projects ~/projects

