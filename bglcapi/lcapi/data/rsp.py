from struct import (unpack_from, calcsize, error)


def generic_result(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


join_mode = generic_result
join_status = generic_result
join = generic_result
confirm_status = generic_result


def send(data: bytes, offset: int = 0):
    FORMAT = '<HI'
    result, uplink_counter = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'result': result, 'uplink_counter': uplink_counter}
    return payload, offset


def read(data: bytes, offset: int = 0):
    FORMAT = '<HBB'
    result, port, data_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    _data_value = data[offset:offset + data_len]
    offset += data_len

    if len(_data_value) < data_len:
        raise error

    payload = {'result': result, 'port': port, 'data': _data_value}
    return payload, offset
