import atexit
import os
import threading
import time

from evdev import InputDevice, categorize, ecodes
from hid import ecodes_to_hid
from hid import keyboard as fake_keyboard
from hid.text_to_hid import UnsupportedCharacterError, convert, process_string
from loguru import logger

# Keyboard device path
KEYBOARD_DEVICE = "/dev/input/event8"  # Replace with your device path
# USB Gadget path for emulating keyboard
GADGET_PATH = "/dev/hidg0"  # Replace with your gadget path

FILE_PATH = "text_to_keyboard.txt"  # Replace with the path to your file


def read_and_process_file(file_path, language):
    with open(file_path, "r") as file:
        content = file.read()
    processed_content = process_string(content, language)
    return processed_content


def cleanup():
    logger.info("Program is about to exit, releasing all keys...")
    fake_keyboard.release_keys(
        GADGET_PATH,
    )


def send_text_as_keystrokes(text: str, language: str):
    for char in text:
        try:
            keystroke = convert(char, language)
            if keystroke:
                fake_keyboard.send_keystroke(GADGET_PATH, keystroke)
                time.sleep(0.05)  # Small delay between keystrokes
        except UnsupportedCharacterError as e:
            logger.error(f"Failed to convert character: {e}")


def handle_file_input():
    while True:
        if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
            text_to_send = read_and_process_file(
                FILE_PATH, "en-US"
            )  # Assuming en-US layout
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


if __name__ == "__main__":
    main()
