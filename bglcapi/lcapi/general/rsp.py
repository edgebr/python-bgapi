from struct import (unpack_from, calcsize, error)


def generic_result(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


attention = generic_result
reset = generic_result
