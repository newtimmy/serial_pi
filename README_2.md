# place the tcp_ip_serial_server_rasp_pi.py server on your rasppi

scp C:\local_path\tcp_ip_serial_server_rasp_pi.py <user>@<raspberry-ip>:/home/<user>

# create server_service file that will be scheduled automatically

<rasppi-user>@<rasppi-ip-adress>:/etc/systemd/system $ cat serial_tcp_server.service
[Unit]
Description=Serial to TCP Server
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/<rasppi-user>/tcp_ip_serial_server_rasp_pi.py
WorkingDirectory=/home/timm/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=<rasppi-user>

[Install]
WantedBy=multi-user.target

# setup and enable your service

sudo systemctl daemon-reload
sudo systemctl enable serial_tcp_server.service

# Check your service status, if necesary

systemctl status serial_tcp_server.service

# Check your process log for any issue that might happen:

journalctl -u serial_tcp_server.service

