from struct import (unpack_from, calcsize, error)


def generic_result(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


join = generic_result
flush_mac_commands = generic_result
flushed_mac_commands = generic_result


def ack(data: bytes, offset: int = 0):
    FORMAT = '<I'
    downlink_counter, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'downlink_counter': downlink_counter}
    return payload, offset


def downlink(data: bytes, offset: int = 0):
    FORMAT = '<IBB'
    downlink_counter, port, data_len = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    _data_value = data[offset:offset + data_len]
    offset += data_len

    if (len(_data_value) < data_len):
        raise error

    payload = {
        'downlink_counter': downlink_counter,
        'port': port,
        'data': _data_value
    }
    return payload, offset


def send(data: bytes, offset: int = 0):
    FORMAT = '<I'
    uplink_counter, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {'uplink_counter': uplink_counter}
    return payload, offset
