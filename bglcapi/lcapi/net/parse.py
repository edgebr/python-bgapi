from struct import (unpack_from, calcsize)

from bglcapi.types import (MessageType, MessageId)

from . import rsp
from . import evt

PARSE_MAP = {
    MessageType.LORA_COMMAND_RESPONSE: {
        MessageId.ADR: rsp.adr,
        MessageId.CLASS: rsp.nclass,
        MessageId.JOIN_RECEIVE_DELAY_1: rsp.join_receive_delay_1,
        MessageId.JOIN_RECEIVE_DELAY_2: rsp.join_receive_delay_2,
        MessageId.RECEIVE_DELAY_1: rsp.receive_delay_1,
        MessageId.RECEIVE_DELAY_2: rsp.receive_delay_2,
        MessageId.DATARATE: rsp.datarate,
        MessageId.RX2_CHANNEL: rsp.rx2_channel,
        MessageId.PNM: rsp.pnm,
        MessageId.TX_POWER: rsp.tx_power,
        MessageId.CHANNEL_MASK: rsp.channel_mask,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
