from struct import (unpack_from, calcsize)


def find_attribute(data: bytes, offset: int = 0):
    FORMAT = '<HH'
    result, sent_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def read_attribute_type(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'type': data[offset:offset + n],
    }
    offset += n
    return payload, offset


def read_attribute_value(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, n = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'value': data[offset:offset + n],
    }
    offset += n
    return payload, offset


def send_characteristic_notification(data: bytes, offset: int = 0):
    FORMAT = '<HH'
    result, sent_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def send_user_read_response(data: bytes, offset: int = 0):
    FORMAT = '<HH'
    result, sent_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
        'sent_len': sent_len,
    }
    return payload, offset


def send_user_write_response(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def set_capabilities(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


def write_attribute_value(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset
