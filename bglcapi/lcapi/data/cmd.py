from struct import pack

from bglcapi.base_command import command
from bglcapi.utils import address_to_bytes
from bglcapi.types import (MessageType, MessageClass, MessageId)


def join_mode(mode):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.JOIN_MODE.value
    payload = pack('<B', mode)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def join_status():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.JOIN_STATUS.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def join():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.JOIN.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def send(port, confirmed, data_value):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.SEND.value
    payload = pack('<BBB', port, confirmed,
                   len(data_value)) + bytes(data_value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def confirm_status():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.CONFIRM_STATUS.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def read():
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.DATA.value
    MSG_ID = MessageId.READ.value
    payload = b''
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
