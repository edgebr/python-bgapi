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
send = generic_result


def read(data: bytes, offset: int = 0):
    FORMAT = '<HIBB'
    result, downlink_counter, port, data_len = unpack_from(FORMAT,
                                                           data,
                                                           offset=offset)
    offset += calcsize(FORMAT)
    _data_value = data[offset:offset + data_len]
    offset += data_len

    if len(_data_value) < data_len:
        raise error

    payload = {
        'result': result,
        'downlink_counter': downlink_counter,
        'port': port,
        'data': _data_value
    }
    return payload, offset
