from struct import pack

from bglcapi.base_command import command
from bglcapi.types import (MessageType, MessageClass)


def close(connection):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_CONNECTION.value
    MSG_ID = 0x04
    payload = pack('<B', connection)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def disable_slave_latency(connection, disable):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_CONNECTION.value
    MSG_ID = 0x02
    payload = pack('<BB', connection, disable)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def get_rssi(connection):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_CONNECTION.value
    MSG_ID = 0x01
    payload = pack('<B', connection)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_parameters(connection, min_interval, max_interval, latency, timeout):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_CONNECTION.value
    MSG_ID = 0x00
    payload = pack('<BHHHH', connection, min_interval, max_interval, latency,
                   timeout)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_phy(connection, phy):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.LE_CONNECTION.value
    MSG_ID = 0x03
    payload = pack('<BB', connection, phy)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
