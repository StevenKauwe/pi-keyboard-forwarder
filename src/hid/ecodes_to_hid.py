from evdev import ecodes
from hid import keycodes as hid


class Error(Exception):
    pass


class UnrecognizedKeyCodeError(Error):
    pass


_MODIFIER_KEYCODES = [
    ecodes.KEY_LEFTCTRL,
    ecodes.KEY_LEFTSHIFT,
    ecodes.KEY_LEFTALT,
    ecodes.KEY_LEFTMETA,
    ecodes.KEY_RIGHTCTRL,
    ecodes.KEY_RIGHTSHIFT,
    ecodes.KEY_RIGHTALT,
    ecodes.KEY_RIGHTMETA,
]


_MAPPING = {
    ecodes.KEY_LEFTCTRL: hid.KEYCODE_LEFT_CTRL,
    ecodes.KEY_LEFTSHIFT: hid.KEYCODE_LEFT_SHIFT,
    ecodes.KEY_LEFTALT: hid.KEYCODE_LEFT_ALT,
    ecodes.KEY_LEFTMETA: hid.KEYCODE_LEFT_META,
    ecodes.KEY_RIGHTCTRL: hid.KEYCODE_RIGHT_CTRL,
    ecodes.KEY_RIGHTSHIFT: hid.KEYCODE_RIGHT_SHIFT,
    ecodes.KEY_RIGHTALT: hid.KEYCODE_RIGHT_ALT,
    ecodes.KEY_RIGHTMETA: hid.KEYCODE_RIGHT_META,
    ecodes.KEY_A: hid.KEYCODE_A,
    ecodes.KEY_B: hid.KEYCODE_B,
    ecodes.KEY_C: hid.KEYCODE_C,
    ecodes.KEY_D: hid.KEYCODE_D,
    ecodes.KEY_E: hid.KEYCODE_E,
    ecodes.KEY_F: hid.KEYCODE_F,
    ecodes.KEY_G: hid.KEYCODE_G,
    ecodes.KEY_H: hid.KEYCODE_H,
    ecodes.KEY_I: hid.KEYCODE_I,
    ecodes.KEY_J: hid.KEYCODE_J,
    ecodes.KEY_K: hid.KEYCODE_K,
    ecodes.KEY_L: hid.KEYCODE_L,
    ecodes.KEY_M: hid.KEYCODE_M,
    ecodes.KEY_N: hid.KEYCODE_N,
    ecodes.KEY_O: hid.KEYCODE_O,
    ecodes.KEY_P: hid.KEYCODE_P,
    ecodes.KEY_Q: hid.KEYCODE_Q,
    ecodes.KEY_R: hid.KEYCODE_R,
    ecodes.KEY_S: hid.KEYCODE_S,
    ecodes.KEY_T: hid.KEYCODE_T,
    ecodes.KEY_U: hid.KEYCODE_U,
    ecodes.KEY_V: hid.KEYCODE_V,
    ecodes.KEY_W: hid.KEYCODE_W,
    ecodes.KEY_X: hid.KEYCODE_X,
    ecodes.KEY_Y: hid.KEYCODE_Y,
    ecodes.KEY_Z: hid.KEYCODE_Z,
    ecodes.KEY_1: hid.KEYCODE_NUMBER_1,
    ecodes.KEY_2: hid.KEYCODE_NUMBER_2,
    ecodes.KEY_3: hid.KEYCODE_NUMBER_3,
    ecodes.KEY_4: hid.KEYCODE_NUMBER_4,
    ecodes.KEY_5: hid.KEYCODE_NUMBER_5,
    ecodes.KEY_6: hid.KEYCODE_NUMBER_6,
    ecodes.KEY_7: hid.KEYCODE_NUMBER_7,
    ecodes.KEY_8: hid.KEYCODE_NUMBER_8,
    ecodes.KEY_9: hid.KEYCODE_NUMBER_9,
    ecodes.KEY_0: hid.KEYCODE_NUMBER_0,
    ecodes.KEY_ENTER: hid.KEYCODE_ENTER,
    ecodes.KEY_ESC: hid.KEYCODE_ESCAPE,
    ecodes.KEY_BACKSPACE: hid.KEYCODE_BACKSPACE_DELETE,
    ecodes.KEY_TAB: hid.KEYCODE_TAB,
    ecodes.KEY_SPACE: hid.KEYCODE_SPACEBAR,
    ecodes.KEY_MINUS: hid.KEYCODE_MINUS,
    ecodes.KEY_EQUAL: hid.KEYCODE_EQUAL_SIGN,
    ecodes.KEY_LEFTBRACE: hid.KEYCODE_LEFT_BRACKET,
    ecodes.KEY_RIGHTBRACE: hid.KEYCODE_RIGHT_BRACKET,
    ecodes.KEY_BACKSLASH: hid.KEYCODE_BACKSLASH,
    ecodes.KEY_SEMICOLON: hid.KEYCODE_SEMICOLON,
    ecodes.KEY_APOSTROPHE: hid.KEYCODE_SINGLE_QUOTE,
    ecodes.KEY_GRAVE: hid.KEYCODE_ACCENT_GRAVE,
    ecodes.KEY_COMMA: hid.KEYCODE_COMMA,
    ecodes.KEY_DOT: hid.KEYCODE_PERIOD,
    ecodes.KEY_SLASH: hid.KEYCODE_FORWARD_SLASH,
    ecodes.KEY_CAPSLOCK: hid.KEYCODE_CAPS_LOCK,
    ecodes.KEY_F1: hid.KEYCODE_F1,
    ecodes.KEY_F2: hid.KEYCODE_F2,
    ecodes.KEY_F3: hid.KEYCODE_F3,
    ecodes.KEY_F4: hid.KEYCODE_F4,
    ecodes.KEY_F5: hid.KEYCODE_F5,
    ecodes.KEY_F6: hid.KEYCODE_F6,
    ecodes.KEY_F7: hid.KEYCODE_F7,
    ecodes.KEY_F8: hid.KEYCODE_F8,
    ecodes.KEY_F9: hid.KEYCODE_F9,
    ecodes.KEY_F10: hid.KEYCODE_F10,
    ecodes.KEY_F11: hid.KEYCODE_F11,
    ecodes.KEY_F12: hid.KEYCODE_F12,
    ecodes.KEY_SYSRQ: hid.KEYCODE_PRINT_SCREEN,
    ecodes.KEY_SCROLLLOCK: hid.KEYCODE_SCROLL_LOCK,
    ecodes.KEY_PAUSE: hid.KEYCODE_PAUSE_BREAK,
    ecodes.KEY_INSERT: hid.KEYCODE_INSERT,
    ecodes.KEY_HOME: hid.KEYCODE_HOME,
    ecodes.KEY_PAGEUP: hid.KEYCODE_PAGE_UP,
    ecodes.KEY_DELETE: hid.KEYCODE_DELETE,
    ecodes.KEY_END: hid.KEYCODE_END,
    ecodes.KEY_PAGEDOWN: hid.KEYCODE_PAGE_DOWN,
    ecodes.KEY_RIGHT: hid.KEYCODE_RIGHT_ARROW,
    ecodes.KEY_LEFT: hid.KEYCODE_LEFT_ARROW,
    ecodes.KEY_DOWN: hid.KEYCODE_DOWN_ARROW,
    ecodes.KEY_UP: hid.KEYCODE_UP_ARROW,
    ecodes.KEY_CLEAR: hid.KEYCODE_CLEAR,
    ecodes.KEY_NUMLOCK: hid.KEYCODE_NUM_LOCK,
    ecodes.KEY_KPASTERISK: hid.KEYCODE_NUMPAD_MULTIPLY,
    ecodes.KEY_KPSLASH: hid.KEYCODE_NUMPAD_DIVIDE,
    ecodes.KEY_KPMINUS: hid.KEYCODE_NUMPAD_MINUS,
    ecodes.KEY_KPPLUS: hid.KEYCODE_NUMPAD_PLUS,
    ecodes.KEY_KPENTER: hid.KEYCODE_NUMPAD_ENTER,
    ecodes.KEY_KP1: hid.KEYCODE_NUMPAD_1,
    ecodes.KEY_KP2: hid.KEYCODE_NUMPAD_2,
    ecodes.KEY_KP3: hid.KEYCODE_NUMPAD_3,
    ecodes.KEY_KP4: hid.KEYCODE_NUMPAD_4,
    ecodes.KEY_KP5: hid.KEYCODE_NUMPAD_5,
    ecodes.KEY_KP6: hid.KEYCODE_NUMPAD_6,
    ecodes.KEY_KP7: hid.KEYCODE_NUMPAD_7,
    ecodes.KEY_KP8: hid.KEYCODE_NUMPAD_8,
    ecodes.KEY_KP9: hid.KEYCODE_NUMPAD_9,
    ecodes.KEY_KP0: hid.KEYCODE_NUMPAD_0,
    ecodes.KEY_KPDOT: hid.KEYCODE_NUMPAD_DOT,
    ecodes.KEY_102ND: hid.KEYCODE_102ND,
    ecodes.KEY_CONTEXT_MENU: hid.KEYCODE_CONTEXT_MENU,
    ecodes.KEY_F13: hid.KEYCODE_F13,
    ecodes.KEY_F14: hid.KEYCODE_F14,
    ecodes.KEY_F15: hid.KEYCODE_F15,
    ecodes.KEY_F16: hid.KEYCODE_F16,
    ecodes.KEY_F17: hid.KEYCODE_F17,
    ecodes.KEY_F18: hid.KEYCODE_F18,
    ecodes.KEY_F19: hid.KEYCODE_F19,
    ecodes.KEY_F20: hid.KEYCODE_F20,
    ecodes.KEY_F21: hid.KEYCODE_F21,
    ecodes.KEY_F22: hid.KEYCODE_F22,
    ecodes.KEY_F23: hid.KEYCODE_F23,
    ecodes.KEY_EXECUTE: hid.KEYCODE_EXECUTE,
    ecodes.KEY_HELP: hid.KEYCODE_HELP,
    ecodes.KEY_SELECT: hid.KEYCODE_SELECT,
    ecodes.KEY_RO: hid.KEYCODE_INTL_RO,
    ecodes.KEY_YEN: hid.KEYCODE_INTL_YEN,
    ecodes.KEY_HANGEUL: hid.KEYCODE_HANGEUL,
    ecodes.KEY_HANJA: hid.KEYCODE_HANJA,
    ecodes.KEY_PLAYPAUSE: hid.KEYCODE_MEDIA_PLAY_PAUSE,
    ecodes.KEY_REFRESH: hid.KEYCODE_REFRESH,
}


def convert(keystroke):
    """Converts a JavaScript-esque Keystroke object into a HID Keystroke object.

    Args:
        keystroke: A JavaScript-esque Keystroke object, as defined in
            `app/request_parsers/keystroke.py`

    Returns:
        A HID Keystroke object.

    Raises:
        UnrecognizedKeyCodeError: If the JavaScript-esque Keystroke's keycode is
            unrecognized.
    """
    return hid.Keystroke(
        keycode=_map_keycode(keystroke), modifier=_map_modifier_keys(keystroke)
    )


def _map_modifier_keys(keystroke):
    modifier_bitmask = 0

    if keystroke.left_ctrl_modifier:
        modifier_bitmask |= hid.MODIFIER_LEFT_CTRL
    if keystroke.right_ctrl_modifier:
        modifier_bitmask |= hid.MODIFIER_RIGHT_CTRL

    if keystroke.left_shift_modifier:
        modifier_bitmask |= hid.MODIFIER_LEFT_SHIFT
    if keystroke.right_shift_modifier:
        modifier_bitmask |= hid.MODIFIER_RIGHT_SHIFT

    if keystroke.left_alt_modifier:
        modifier_bitmask |= hid.MODIFIER_LEFT_ALT
    if keystroke.right_alt_modifier:
        modifier_bitmask |= hid.MODIFIER_RIGHT_ALT

    if keystroke.left_meta_modifier:
        modifier_bitmask |= hid.MODIFIER_LEFT_META
    if keystroke.right_meta_modifier:
        modifier_bitmask |= hid.MODIFIER_RIGHT_META

    return modifier_bitmask


def _map_keycode(keystroke):
    # If the current key press is a modifier key and it's the *only* modifier
    # being pressed, treat it as a special case where we remap the HID code to
    # KEYCODE_NONE. This is based on a report that certain KVMs only recognize
    # a modifier keystroke if the HID code is KEYCODE_NONE, but we should verify
    # that it matches behavior from normal USB keyboards.
    if keystroke.code in _MODIFIER_KEYCODES and _count_modifiers(keystroke) == 1:
        return hid.KEYCODE_NONE

    try:
        return _MAPPING[keystroke.code]
    except KeyError as e:
        raise UnrecognizedKeyCodeError(
            f"Unrecognized key code {keystroke.key} {keystroke.code}"
        ) from e


def _count_modifiers(keystroke):
    return (
        int(keystroke.left_ctrl_modifier)
        + int(keystroke.right_ctrl_modifier)
        + int(keystroke.left_shift_modifier)
        + int(keystroke.right_shift_modifier)
        + int(keystroke.left_alt_modifier)
        + int(keystroke.right_alt_modifier)
        + int(keystroke.left_meta_modifier)
        + int(keystroke.right_meta_modifier)
    )
