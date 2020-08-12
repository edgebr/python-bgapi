from struct import (unpack_from, calcsize)

from bglcapi.types import (MessageType, MessageId)

from . import rsp
from . import evt

PARSE_MAP = {
    MessageType.LORA_COMMAND_RESPONSE: {
        MessageId.SET.value: rsp.set,
        MessageId.GET.value: rsp.get,
    },
}


def from_binary(msg_type: int, msg_id: int, data: bytes, offset: int):
    return PARSE_MAP[msg_type][msg_id](data, offset)
