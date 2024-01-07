import execute
from loguru import logger


class Error(Exception):
    pass


class WriteError(Error):
    pass


def _write_to_hid_interface_immediately(hid_path, buffer):
    try:
        with open(hid_path, "ab+") as hid_handle:
            hid_handle.write(bytearray(buffer))
    except BlockingIOError:
        logger.error(
            "Failed to write to HID interface: %s. Is USB cable connected?", hid_path
        )


def write_to_hid_interface(hid_path, buffer):
    # Avoid an unnecessary string formatting call in a write that requires low
    # latency.
    logger.debug(
        f"writing to HID interface {hid_path}: {" ".join([f"{x:#04x}" for x in buffer])}"
    )
    # Writes can hang, for example, when TinyPilot is attempting to write to the
    # mouse interface, but the target system has no GUI. To avoid locking up the
    # main server process, perform the HID interface I/O in a separate process.
    try:
        execute.with_timeout(
            _write_to_hid_interface_immediately,
            args=(hid_path, buffer),
            timeout_in_seconds=0.5,
        )
    except TimeoutError as e:
        raise WriteError(
            f"Failed to write to HID interface: {hid_path}. " "Is USB cable connected?"
        ) from e
