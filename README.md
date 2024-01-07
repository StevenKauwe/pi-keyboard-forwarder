# pi-keyboard-forwarder

## Overview

This is a simple script that forwards keyboard input from a Raspberry Pi to a usb connected computer. Plans to also forward speech-to-text recorded on the pi to the connected computer.

## Setup
This script is intended to be run on a Raspberry Pi. It has been tested on a Raspberry Pi 4 running Raspbian Bullseye.

### Dependencies
- python3
- python3-pip
- python3-venv
- evdev

### Installation
1. Clone this repository
2. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
3. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
4. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
5. Run the script
    ```bash
    python3 main.py
    ```

### Configure to run on startup  [Not Tested At all - writtend by GPT]

To have the script run automatically on startup, you can use a systemd service.

1. Create a new service file in `/etc/systemd/system/` with a `.service` extension. For example, `pi-keyboard-forwarder.service`.

    ```bash
    sudo nano /etc/systemd/system/pi-keyboard-forwarder.service
    ```

2. In the service file, add the following:

    ```ini
    [Unit]
    Description=Pi Keyboard Forwarder

    [Service]
    ExecStart=/path/to/your/venv/bin/python3 /path/to/your/script/main.py
    WorkingDirectory=/path/to/your/script/
    User=pi
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `/path/to/your/venv/` and `/path/to/your/script/` with the actual paths to your virtual environment and script.

3. Save and close the file.

4. Enable the service to start on boot:

    ```bash
    sudo systemctl enable pi-keyboard-forwarder
    ```

5. Start the service:

    ```bash
    sudo systemctl start pi-keyboard-forwarder
    ```

6. Check the status of the service:

    ```bash
    sudo systemctl status pi-keyboard-forwarder
    ```

Now, the script should start automatically every time your Raspberry Pi boots up.

### Connecting to a computer
1. Connect the Raspberry Pi to the computer via USB-C power-port on the Raspberry Pi.
    - This will power the Raspberry Pi and allow it to communicate with the computer.
    - You may get a low-voltage warning on the Raspberry Pi, this may be an issue but I have no idea. :shrug:
2. Plug a USB keyboard into the Raspberry Pi.
3. Plug a USB microphone into the Raspberry Pi.


## Acknowledgements

Thanks to [tiny-pilot](https://github.com/tiny-pilot/tinypilot) for doing the hard work of getting the this working. This is a simplification of their work, with the goal of reducing complexity for a simpler use case of keyboard and speech-to-text forwarding.