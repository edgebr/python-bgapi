from struct import (unpack_from, calcsize, error)

from .types import (MessageClass, ParseError)
from .bgapi import coex
from .bgapi import dfu
from .bgapi import flash
from .bgapi import gatt
from .bgapi import gatt_server
from .bgapi import hardware
from .bgapi import le_connection
from .bgapi import le_gap
from .bgapi import sm
from .bgapi import system
from .bgapi import test
from .bgapi import user
from .lcapi import general
from .lcapi import key
from .lcapi import data
from .lcapi import net

PARSE_MAP = {
    0x20: {
        MessageClass.COEX: coex.parse.from_binary,
        MessageClass.DFU: dfu.parse.from_binary,
        MessageClass.ENDPOINT: None,
        MessageClass.FLASH: flash.parse.from_binary,
        MessageClass.GATT: gatt.parse.from_binary,
        MessageClass.GATT_SERVER: gatt_server.parse.from_binary,
        MessageClass.HARDWARE: hardware.parse.from_binary,
        MessageClass.LE_CONNECTION: le_connection.parse.from_binary,
        MessageClass.LE_GAP: le_gap.parse.from_binary,
        MessageClass.SM: sm.parse.from_binary,
        MessageClass.SYSTEM: system.parse.from_binary,
        MessageClass.TEST: test.parse.from_binary,
        MessageClass.USER: user.parse.from_binary,
    },
    0x78: {
        MessageClass.GENERAL: general.parse.from_binary,
        MessageClass.KEY: key.parse.from_binary,
        MessageClass.DATA: data.parse.from_binary,
        MessageClass.NET: net.parse.from_binary,
    }
}


def from_binary(data: bytes, offset: int = 0):
    FORMAT = '<BBBB'
    _offset = offset
    try:
        msg_type, payload_len, msg_class, msg_id = unpack_from(FORMAT,
                                                               data,
                                                               offset=_offset)
        _offset += calcsize(FORMAT)
        msg_tech = msg_type & 0x78
        if msg_tech in PARSE_MAP and msg_class in PARSE_MAP[msg_tech]:
            payload, _offset = PARSE_MAP[msg_tech][msg_class](msg_type, msg_id,
                                                          data, _offset)
            packet = None 
            if payload != None :
                packet = {
                    'msg_type': msg_type,
                    'payload_len': payload_len,
                    'msg_class': msg_class,
                    'msg_id': msg_id,
                    'payload': payload,
                }
            return packet, _offset
        else :
            return None, _offset
    except error:
        return None, offset
