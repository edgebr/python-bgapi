from struct import pack

from bglcapi.base_command import command
from bglcapi.utils import address_to_bytes
from bglcapi.types import (MessageType, MessageClass, MessageId)


def attention():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GENERAL.value
    MSG_ID = MessageId.ATTENTION.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def reset():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.GENERAL.value
    MSG_ID = MessageId.RESET.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
