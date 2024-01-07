from loguru import logger


class Error(Exception):
    pass


class WriteError(Error):
    pass


def _write_to_hid_interface_immediately(hid_path, buffer):
    try:
        with open(hid_path, "ab+") as hid_handle:
            hid_handle.write(bytearray(buffer))
    except BlockingIOError as e:
        raise WriteError(
            f"Failed to write to HID interface: {hid_path}. Is USB cable connected?"
        ) from e


def write_to_hid_interface(hid_path, buffer):
    buffer_info = " ".join([f"{x:#04x}" for x in buffer])
    logger.debug(f"Writing to HID interface {hid_path}: {buffer_info}")
    _write_to_hid_interface_immediately(hid_path, buffer)
