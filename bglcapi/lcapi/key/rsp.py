from struct import (unpack_from, calcsize, error)


def generic_result(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


set = generic_result


def get(data: bytes, offset: int = 0):
    FORMAT = '<HB'
    result, key_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    _key_value = data[offset:offset + key_len]
    offset += key_len

    if len(_key_value) < key_len:
        raise error

    payload = {
        'result': result,
        'key_value': _key_value,
    }
    return payload, offset
