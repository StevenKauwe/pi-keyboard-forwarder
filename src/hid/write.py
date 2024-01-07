from loguru import logger


class Error(Exception):
    pass


class WriteError(Error):
    pass


def _with_timeout(func, args, timeout_in_seconds, executor):
    future = executor.submit(func, *args)
    return future.result(timeout=timeout_in_seconds)


def _write_to_hid_interface_immediately(hid_path, buffer):
    try:
        with open(hid_path, "ab+") as hid_handle:
            hid_handle.write(bytearray(buffer))
    except BlockingIOError:
        logger.error(
            "Failed to write to HID interface: %s. Is USB cable connected?", hid_path
        )


def write_to_hid_interface(hid_path, buffer, executor):
    buffer_info = " ".join([f"{x:#04x}" for x in buffer])
    logger.debug(f"writing to HID interface {hid_path}: {buffer_info}")
    try:
        _with_timeout(
            _write_to_hid_interface_immediately,
            args=(hid_path, buffer),
            timeout_in_seconds=0.5,
            executor=executor,
        )
    except TimeoutError as e:
        raise WriteError(
            f"Failed to write to HID interface: {hid_path}. Is USB cable connected?"
        ) from e
