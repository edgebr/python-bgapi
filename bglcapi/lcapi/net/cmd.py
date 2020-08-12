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


def join_receive_delay_1(delay):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.JOIN_RECEIVE_DELAY_1.value
    payload = pack('<I', delay)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def join_receive_delay_2(delay):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.JOIN_RECEIVE_DELAY_2.value
    payload = pack('<I', delay)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def receive_delay_1(delay):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.RECEIVE_DELAY_1.value
    payload = pack('<I', delay)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def receive_delay_2(delay):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.RECEIVE_DELAY_2.value
    payload = pack('<I', delay)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def datarate(dr):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.DATARATE.value
    payload = pack('<B', dr)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def rx2_channel(dr, freq):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.RX2_CHANNEL.value
    payload = pack('<BI', dr, freq)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def pnm(mode):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.PNM.value
    payload = pack('<B', mode)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def tx_power(power):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.TX_POWER.value
    payload = pack('<B', power)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)


def channel_mask(mask_value):
    MSG_TYPE = MessageType.LORA_COMMAND_RESPONSE.value
    MSG_CLASS = MessageClass.NET.value
    MSG_ID = MessageId.CHANNEL_MASK.value
    payload = pack('<B', len(mask_value)) + bytes(mask_value)
    return command(MSG_TYPE, MSG_CLASS, MSG_ID, payload)
