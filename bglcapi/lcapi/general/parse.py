from struct import (unpack_from, calcsize)

from bglcapi.types import (MessageType, MessageId)

from . import rsp
from . import evt

PARSE_MAP = {
    MessageType.LORA_COMMAND_RESPONSE: {
        MessageId.ATTENTION.value: rsp.attention,
        MessageId.RESET.value: rsp.reset,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    if msg_type in PARSE_MAP and msg_id in PARSE_MAP[msg_type] :
        return PARSE_MAP[msg_type][msg_id](data, offset)
    else :
        return None, offset
