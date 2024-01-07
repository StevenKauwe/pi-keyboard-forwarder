from hid import write as hid_write
from hid.keycodes import Keystroke


def send_keystroke(keyboard_path, keystroke: Keystroke):
    hid_code, modifier, keystate = (
        keystroke.keycode,
        keystroke.modifier,
        keystroke.keystate,
    )
    # Prepare the report
    report = bytearray(8)
    # Set the modifier
    report[0] = modifier
    # Set the key code
    if keystate == Keystroke.KEY_UP:
        report[2] = 0
    else:
        report[2] = hid_code  # Key pressed
    # Write the report to the HID device
    with open(keyboard_path, "rb+") as hid_file:
        hid_file.write(report)


def release_keys(keyboard_path):
    hid_write.write_to_hid_interface(keyboard_path, [0] * 8)


def send_keystrokes(keyboard_path, keystrokes):
    """Sends multiple keystrokes to the HID interface, one after the other.

    Args:
        keyboard_path: The file path to the keyboard interface.
        keystrokes: A list of HID Keystroke objects.

    Raises:
        WriteError: If a keystroke fails to be written to the HID interface.
    """
    for keystroke in keystrokes:
        send_keystroke(keyboard_path, keystroke)
