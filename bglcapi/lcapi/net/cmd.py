from struct import pack

from bglcapi.base_command import command
from bglcapi.utils import address_to_bytes
from bglcapi.types import (MessageType, MessageClass, MessageId)


def adr(mode):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.ADR.value
    payload = pack('<B', mode)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def nclass(c):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.CLASS.value
    payload = pack('<B', c)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
