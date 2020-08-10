from struct import (unpack_from, calcsize, error)


def get_bt_address(data: bytes, offset: int = 0):
    ADDRESS_SIZE_BYTES = 6
    address = data[offset:offset + ADDRESS_SIZE_BYTES]

    if len(address) < ADDRESS_SIZE_BYTES:
        raise error

    return {'address': address}


def get_counters(data: bytes, offset: int = 0):
    FORMAT = '<HHHHH'
    result, tx_packets, rx_packets, crc_errors, failures = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'tx_packets': tx_packets,
        'rx_packets': rx_packets,
        'crc_errors': crc_errors,
        'failures': failures,
    }
    return payload, offset


def get_random_data(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    _data = data[offset:offset + n]
    offset += n

    if len(_data) < n:
        raise error

    payload = {
        'result': result,
        'data': _data,
    }
    return payload, offset


def halt(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def hello(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def set_bt_address(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def set_device_name(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def set_tx_power(data: bytes, offset: int = 0):
    FORMAT = '<H'
    set_power, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    return {'set_power': set_power}, offset
