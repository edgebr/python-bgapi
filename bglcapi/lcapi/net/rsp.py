from struct import (unpack_from, calcsize, error)


def generic_result(data: bytes, offset: int = 0):
    FORMAT = '<H'
    result, = unpack_from(FORMAT, data, offset=offset)
    offset += calcsize(FORMAT)
    payload = {
        'result': result,
    }
    return payload, offset


adr = generic_result
nclass = generic_result
join_receive_delay_1 = generic_result
join_receive_delay_2 = generic_result
receive_delay_1 = generic_result
receive_delay_2 = generic_result
datarate = generic_result
rx2_channel = generic_result
pnm = generic_result
tx_power = generic_result
channel_mask = generic_result
