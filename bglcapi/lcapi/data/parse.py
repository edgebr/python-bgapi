from struct import (unpack_from, calcsize)

from bglcapi.types import (MessageType, MessageId)

from . import rsp
from . import evt

PARSE_MAP = {
    MessageType.LORA_COMMAND_RESPONSE: {
        MessageId.JOIN_MODE: rsp.join_mode,
        MessageId.JOIN_STATUS: rsp.join_status,
        MessageId.JOIN: rsp.join,
        MessageId.SEND: rsp.send,
        MessageId.CONFIRM_STATUS: rsp.confirm_status,
        MessageId.READ: rsp.read,
    },
    MessageType.LORA_EVENT: {
        MessageId.JOIN: evt.join,
        MessageId.SEND: evt.send,
        MessageId.DOWNLINK: evt.downlink,
        MessageId.ACK: evt.ack,
        MessageId.FLUSH_MAC_COMMANDS: evt.flush_mac_commands,
        MessageId.FLUSHED_MAC_COMMANDS: evt.flushed_mac_commands,
    }
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
