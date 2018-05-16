from struct import (unpack_from, calcsize)

from bgapi.gatt_server.types import CharacteristicStatusFlag
from bgapi.gatt.types import (ClientConfigFlag, AttOpcode)
from bgapi.base import _parse_result


def attribute_value(data: bytes, offset: int = 0):
    FORMAT = '<BHBHB'
    connection, attribute, att_opcode, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'attribute': attribute,
        'att_opcode': AttOpcode(att_opcode),
        'offset': _offset,
        'value': value,
    }

    return payload, offset


def characteristic_status(data: bytes, offset: int = 0):
    FORMAT = '<BHBH'
    connection, characteristic, status_flags, client_config_flags = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'status_flags': CharacteristicStatusFlag(status_flags),
        'client_config_flags': ClientConfigFlag(client_config_flags),
    }

    return payload, offset


def execute_write_completed(data: bytes, offset: int = 0):
    FORMAT = '<B'
    connection, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    result, offset = _parse_result(data, offset)

    payload = {
        'connection': connection,
        'result': result,
    }

    return payload, offset


def user_read_request(data: bytes, offset: int = 0):
    FORMAT = '<BHBH'
    connection, characteristic, att_opcode, _offset = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'att_opcode': AttOpcode(att_opcode),
        'offset': _offset,
    }

    return payload, offset


def user_write_request(data: bytes, offset: int = 0):
    FORMAT = '<BHBHB'
    connection, characteristic, att_opcode, _offset, n = unpack_from(
        FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    value = data[offset:offset + n]
    offset += n

    payload = {
        'connection': connection,
        'characteristic': characteristic,
        'att_opcode': AttOpcode(att_opcode),
        'offset': _offset,
        'value': value,
    }

    return payload, offset
