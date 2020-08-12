from struct import pack

from bglcapi.base_command import command
from bglcapi.types import (MessageType, MessageClass)


def flash_set_address(address):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DFU.value
    MSG_ID = 0x01
    payload = pack('<I', address)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def flash_upload(data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DFU.value
    MSG_ID = 0x02
    payload = data
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def flash_upload_finish():
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DFU.value
    MSG_ID = 0x03
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def reset(dfu):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DFU.value
    MSG_ID = 0x00
    payload = pack('<B', dfu)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
