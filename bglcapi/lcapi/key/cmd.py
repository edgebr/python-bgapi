from struct import pack

from bglcapi.base_command import command
from bglcapi.utils import address_to_bytes
from bglcapi.types import (MessageType, MessageClass, MessageId)


def set(key_id, key_value):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE
    MSG_CLASS = MessageClass.KEY.value
    MSG_ID = MessageId.SET.value
    payload = pack('<BB', key_id, len(key_value)) + bytes(key_value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def get(key_id):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE
    MSG_CLASS = MessageClass.KEY.value
    MSG_ID = MessageId.GET.value
    payload = pack('<B', key_id)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
