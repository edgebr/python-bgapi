from bglcapi import (bgapi, lcapi, from_binary)


def print_bytes(data):
    for by in data:
        print(f'{by:02X} ', end='')
    print("\n")


def print_status(data1, data2):
    print("expected > ", end='')
    print_bytes(data1)
    print("result   > ", end='')
    print_bytes(data2)


def check_rsp_evt_header(obj, data):
    return obj['msg_type'] == data[0] and obj['payload_len'] == data[
        1] and obj['msg_class'] == data[2] and obj['msg_id'] == data[3]


def test_lcapi_data():
    cmd_join_mode = b'\x78\x01\x02\x00\x01'
    cmd_join_status = b'\x78\x00\x02\x01'
    cmd_join = b'\x78\x00\x02\x02'
    cmd_send = b'\x78\x0B\x02\x03\x02\x01\x08\x01\x02\x03\x04\x05\x06\x07\x08'
    cmd_confirm_status = b'\x78\x00\x02\x04'
    cmd_read = b'\x78\x00\x02\x05'

    if cmd_join_mode != lcapi.data.cmd.join_mode(0x01):
        print(f"Error creating join mode command")
        print_status(cmd_join_mode, lcapi.data.cmd.join_mode(0x01))

    if cmd_join_status != lcapi.data.cmd.join_status():
        print("Error creating join status command")
        print_status(cmd_join_status, lcapi.data.cmd.join_status())

    if cmd_join != lcapi.data.cmd.join():
        print("Error creating join command")
        print_status(cmd_join, lcapi.data.cmd.join())

    if cmd_send != lcapi.data.cmd.send(0x02, 0x01,
                                       b'\x01\x02\x03\x04\x05\x06\x07\x08'):
        print("Error creating send command")
        print_status(
            cmd_send,
            lcapi.data.cmd.send(0x02, 0x01,
                                b'\x01\x02\x03\x04\x05\x06\x07\x08'))

    if cmd_confirm_status != lcapi.data.cmd.confirm_status():
        print("Error creating confirm status command")
        print_status(cmd_confirm_status, lcapi.data.cmd.confirm_status())

    if cmd_read != lcapi.data.cmd.read():
        print("Error creating read command")
        print_status(cmd_read, lcapi.data.cmd.read())

    rsp_join_mode = b'\x78\x02\x02\x00\x02\x00'
    rsp_join_status = b'\x78\x02\x02\x01\x01\x00'
    rsp_join = b'\x78\x02\x02\x02\x00\x00'
    rsp_send = b'\x78\x06\x02\x03\x00\x00\x64\x00\x00\x00'
    rsp_confirm_status = b'\x78\x02\x02\x04\x00\x00'
    rsp_read = b'\x78\x0C\x02\x05\x00\x00\x03\x08\x01\x02\x03\x04\x05\x06\x07\x08'
    evt_join = b'\xF8\x02\x02\x02\x04\x00'
    evt_ack = b'\xF8\x04\x02\x06\x0B\x00\x00\x00'
    evt_downlink = b'\xF8\x16\x02\x07\xD7\x01\x00\x00\x07\x10\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    evt_send = b'\xF8\x04\x02\x03\x20\x10\x00\x00'

    obj, n = from_binary(rsp_join_mode)
    if not check_rsp_evt_header(
            obj, rsp_join_mode) or (obj['payload']['result'] != 2):
        print("Error creating rsp join mode object")
        print(obj)
        print_bytes(rsp_join_mode)

    obj, n = from_binary(rsp_join_status)
    if not check_rsp_evt_header(
            obj, rsp_join_status) or (obj['payload']['result'] != 1):
        print("Error creating rsp join status object")
        print(obj)
        print_bytes(rsp_join_status)

    obj, n = from_binary(rsp_join)
    if not check_rsp_evt_header(obj,
                                rsp_join) or (obj['payload']['result'] != 0):
        print("Error creating rsp join object")
        print(obj)
        print_bytes(rsp_join)

    obj, n = from_binary(rsp_send)
    if not check_rsp_evt_header(
            obj, rsp_send) or (obj['payload']['result'] !=
                               0) or (obj['payload']['uplink_counter'] != 100):
        print("Error creating rsp join object")
        print(obj)
        print_bytes(rsp_send)

    obj, n = from_binary(rsp_confirm_status)
    if not check_rsp_evt_header(
            obj, rsp_confirm_status) or (obj['payload']['result'] != 0):
        print("Error creating rsp confirm status object")
        print(obj)
        print_bytes(rsp_confirm_status)

    obj, n = from_binary(rsp_read)
    if not check_rsp_evt_header(
            obj, rsp_read) or (obj['payload']['result'] != 0) or (
                obj['payload']['port'] != 3
            ) or (len(obj['payload']['data']) != 8) or (
                obj['payload']['data'] != b'\x01\x02\x03\x04\x05\x06\x07\x08'):
        print("Error creating rsp read object")
        print(obj)
        print_bytes(rsp_read)

    obj, n = from_binary(evt_join)
    if not check_rsp_evt_header(obj,
                                evt_join) or (obj['payload']['result'] != 4):
        print("Error creating evt join object")
        print(obj)
        print_bytes(evt_join)

    obj, n = from_binary(evt_ack)
    if not check_rsp_evt_header(
            obj, evt_ack) or (obj['payload']['downlink_counter'] != 11):
        print("Error creating evt ack object")
        print(obj)
        print_bytes(evt_ack)

    obj, n = from_binary(evt_downlink)
    if not check_rsp_evt_header(obj, evt_downlink) or (
            obj['payload']['downlink_counter'] != 471
    ) or (obj['payload']['port'] != 7) or (
            len(obj['payload']['data']) != 16
    ) or (obj['payload']['data'] !=
          b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'):
        print("Error creating evt downlink object")
        print(obj)
        print_bytes(evt_downlink)

    obj, n = from_binary(evt_send)
    if not check_rsp_evt_header(
            obj, evt_send) or (obj['payload']['uplink_counter'] != 4128):
        print("Error creating evt send object")
        print(obj)
        print_bytes(evt_send)

    print("End of lcapi data test")


if __name__ == "__main__":
    test_lcapi_data()
