from struct import pack

from bglcapi.base_command import command
from bglcapi.types import (MessageType, MessageClass)


def message_to_target(data):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.USER.value
    MSG_ID = 0x00
    payload = pack('<B', len(data)) + bytes(data)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
