from struct import pack

from bglcapi.base_command import command
from bglcapi.types import (MessageType, MessageClass)


def set_lazy_soft_timer(time, slack, handle, single_shot):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.HARDWARE.value
    MSG_ID = 0x0c
    payload = pack('<IIBB', time, slack, handle, single_shot)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def set_soft_timer(time, handle, single_shot):
    MSG_TYPE = MessageType.COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.HARDWARE.value
    MSG_ID = 0x00
    payload = pack('<IBB', time, handle, single_shot)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
