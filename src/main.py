import atexit
import os
import threading
import time

from evdev import InputDevice, categorize, ecodes
from loguru import logger

from hid import ecodes_to_hid
from hid import keyboard as fake_keyboard
from hid.text_to_hid import UnsupportedCharacterError, convert

# Keyboard device path
KEYBOARD_DEVICE = "/dev/input/event8"  # Replace with your device path
# USB Gadget path for emulating keyboard
GADGET_PATH = "/dev/hidg0"  # Replace with your gadget path

FILE_PATH = "text_to_keyboard.txt"  # Replace with the path to your file


def cleanup():
    logger.info("Program is about to exit, releasing all keys...")
    fake_keyboard.release_keys(
        GADGET_PATH,
    )


def send_text_as_keystrokes(text: str, language: str):
    for char in text:
        try:
            keystroke = convert(char, language)
            logger.debug(f"Sending keystroke for text: {keystroke}")
            if keystroke:
                logger.debug(f"Sending keystroke: {keystroke} (DOWN))")
                keystroke.keystate = 1
                fake_keyboard.send_keystroke(GADGET_PATH, keystroke)

                logger.debug(f"Sending keystroke: {keystroke} (UP))")
                keystroke.keystate = 0
                fake_keyboard.send_keystroke(GADGET_PATH, keystroke)

                time.sleep(0.05)  # Small delay between keystrokes
        except UnsupportedCharacterError as e:
            logger.error(f"Failed to convert character: {e}")


def handle_file_input():
    while True:
        if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
            with open(FILE_PATH, "r") as file:
                text_to_send = file.read().rstrip("\n")
            logger.info(
                f"File {FILE_PATH} has content:\n{text_to_send}\n\nSending as keystrokes..."
            )
            send_text_as_keystrokes(text_to_send, "en-US")

            # Wipe the file content after sending
            with open(FILE_PATH, "w") as file:
                file.write("")

        # Insert a delay to prevent constant polling of the file
        time.sleep(1)


def main():
    atexit.register(cleanup)
    keyboard = InputDevice(KEYBOARD_DEVICE)
    logger.info(f"Listening on device: {keyboard.name}")

    # Start a separate thread for file handling
    file_thread = threading.Thread(target=handle_file_input)
    file_thread.start()

    # Continue with the main thread for keyboard event handling
    try:
        for event in keyboard.read_loop():
            logger.debug(f"Received event: {event}")
            if event.type == ecodes.EV_KEY:
                key_event = categorize(event)
                hid_keystroke = ecodes_to_hid.convert(key_event)
                logger.debug(f"Converted HID event: {hid_keystroke} from {key_event}")
                try:
                    fake_keyboard.send_keystroke(GADGET_PATH, hid_keystroke)
                except Exception as e:
                    logger.error(f"Failed to write key event: {e}")
    except KeyboardInterrupt:
        # If the program is terminated with Ctrl+C, make sure to join the file_thread
        file_thread.join()


if __name__ == "__main__":
    main()
