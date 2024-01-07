import atexit

from evdev import InputDevice, categorize, ecodes
from hid import ecodes_to_hid
from hid import keyboard as fake_keyboard
from loguru import logger

# Keyboard device path
KEYBOARD_DEVICE = "/dev/input/event8"  # Replace with your device path
# USB Gadget path for emulating keyboard
GADGET_PATH = "/dev/hidg0"  # Replace with your gadget path


def cleanup():
    logger.info("Program is about to exit, releasing all keys...")
    fake_keyboard.release_keys(
        GADGET_PATH,
    )


def main():
    atexit.register(cleanup)
    keyboard = InputDevice(KEYBOARD_DEVICE)
    logger.info(f"Listening on device: {keyboard.name}")

    for event in keyboard.read_loop():
        logger.debug(f"Received event: {event}")
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            # Convert the input event to a HID event
            hid_keystroke = ecodes_to_hid.convert(key_event)
            logger.debug(f"Converted HID event: {hid_keystroke} from {key_event}")
            # Send the HID event
            try:
                fake_keyboard.send_keystroke(GADGET_PATH, hid_keystroke)
            except Exception as e:
                logger.error(f"Failed to write key event: {e}")


if __name__ == "__main__":
    main()
