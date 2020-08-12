from bglcapi import (bgapi, lcapi, from_binary)
import unittest


def check_rsp_evt_header(obj, data):
    return obj['msg_type'] == data[0] and obj['payload_len'] == data[
        1] and obj['msg_class'] == data[2] and obj['msg_id'] == data[3]


class TestLcapiGeneralCommands(unittest.TestCase):
    def test_cmd_attention(self):
        cmd = b'\x78\x00\x00\x00'
        self.assertEqual(cmd, lcapi.general.cmd.attention())

    def test_cmd_reset(self):
        cmd = b'\x78\x00\x00\x01'
        self.assertEqual(cmd, lcapi.general.cmd.reset())


class TestLcapiGeneralResponses(unittest.TestCase):
    def test_rsp_attention(self):
        rsp = b'\x78\x02\x00\x00\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_reset(self):
        rsp = b'\x78\x02\x00\x01\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])


class TestLcapiKeyCommands(unittest.TestCase):
    def test_cmd_set(self):
        cmd = b'\x78\x0A\x01\x00\x08\x08\x01\x02\x03\xFF\xF3\xF7\xF8\x89'
        self.assertEqual(
            cmd, lcapi.key.cmd.set(0x08, b'\x01\x02\x03\xFF\xF3\xF7\xF8\x89'))

    def test_cmd_get(self):
        cmd = b'\x78\x01\x01\x01\x0A'
        self.assertEqual(cmd, lcapi.key.cmd.get(10))


class TestLcapiKeyResponses(unittest.TestCase):
    def test_rsp_set(self):
        rsp = b'\x78\x02\x01\x00\x01\x04'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0x0401, obj['payload']['result'])

    def test_rsp_get(self):
        rsp = b'\x78\x0B\x01\x01\x00\x00\x08\x01\x02\x03\x04\x05\x06\x07\x08'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0x0000, obj['payload']['result'])
        self.assertEqual(8, len(obj['payload']['key_value']))
        self.assertEqual(b'\x01\x02\x03\x04\x05\x06\x07\x08',
                         obj['payload']['key_value'])


class TestLcapiDataCommands(unittest.TestCase):
    def test_cmd_join_mode(self):
        cmd = b'\x78\x01\x02\x00\x01'
        self.assertEqual(cmd, lcapi.data.cmd.join_mode(0x01))

    def test_cmd_join_status(self):
        cmd = b'\x78\x00\x02\x01'
        self.assertEqual(cmd, lcapi.data.cmd.join_status())

    def test_cmd_join(self):
        cmd = b'\x78\x00\x02\x02'
        self.assertEqual(cmd, lcapi.data.cmd.join())

    def test_cmd_send(self):
        cmd = b'\x78\x0B\x02\x03\x02\x01\x08\x01\x02\x03\x04\x05\x06\x07\x08'
        self.assertEqual(
            cmd,
            lcapi.data.cmd.send(0x02, 0x01,
                                b'\x01\x02\x03\x04\x05\x06\x07\x08'))

    def test_cmd_confirm_status(self):
        cmd = b'\x78\x00\x02\x04'
        self.assertEqual(cmd, lcapi.data.cmd.confirm_status())

    def test_cmd_read(self):
        cmd = b'\x78\x00\x02\x05'
        self.assertEqual(cmd, lcapi.data.cmd.read())


class TestLcapiDataResponse(unittest.TestCase):
    def test_rsp_join_mode(self):
        rsp = b'\x78\x02\x02\x00\x02\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(2, obj['payload']['result'])

    def test_rsp_join_status(self):
        rsp = b'\x78\x02\x02\x01\x01\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(1, obj['payload']['result'])

    def test_rsp_join(self):
        rsp = b'\x78\x02\x02\x02\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_send(self):
        rsp = b'\x78\x06\x02\x03\x00\x00\x64\x00\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])
        self.assertEqual(100, obj['payload']['uplink_counter'])

    def test_rsp_confirm_status(self):
        rsp = b'\x78\x02\x02\x04\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_read(self):
        rsp = b'\x78\x0C\x02\x05\x00\x00\x03\x08\x01\x02\x03\x04\x05\x06\x07\x08'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])
        self.assertEqual(3, obj['payload']['port'])
        self.assertEqual(8, len(obj['payload']['data']))
        self.assertEqual(b'\x01\x02\x03\x04\x05\x06\x07\x08',
                         obj['payload']['data'])


class TestLcapiDataEvent(unittest.TestCase):
    def test_evt_join(self):
        evt = b'\xF8\x02\x02\x02\x04\x00'
        obj, n = from_binary(evt)
        self.assertTrue(check_rsp_evt_header(obj, evt))
        self.assertEqual(4, obj['payload']['result'])

    def test_evt_ack(self):
        evt = b'\xF8\x04\x02\x06\x0B\x00\x00\x00'
        obj, n = from_binary(evt)
        self.assertTrue(check_rsp_evt_header(obj, evt))
        self.assertEqual(11, obj['payload']['downlink_counter'])

    def test_evt_downlink(self):
        evt = b'\xF8\x16\x02\x07\xD7\x01\x00\x00\x07\x10\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
        obj, n = from_binary(evt)
        self.assertTrue(check_rsp_evt_header(obj, evt))
        self.assertEqual(471, obj['payload']['downlink_counter'])
        self.assertEqual(7, obj['payload']['port'])
        self.assertEqual(16, len(obj['payload']['data']))
        self.assertEqual(
            b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F',
            obj['payload']['data'])

    def test_evt_send(self):
        evt = b'\xF8\x04\x02\x03\x20\x10\x00\x00'
        obj, n = from_binary(evt)
        self.assertTrue(check_rsp_evt_header(obj, evt))
        self.assertEqual(4128, obj['payload']['uplink_counter'])


class TestLcapiNetCommand(unittest.TestCase):
    def test_cmd_adr(self):
        cmd = b'\x78\x01\x03\x00\x01'
        self.assertEqual(cmd, lcapi.net.cmd.adr(0x01))

    def test_cmd_class(self):
        cmd = b'\x78\x01\x03\x01\x02'
        self.assertEqual(cmd, lcapi.net.cmd.nclass(0x02))

    def test_cmd_join_receive_delay_1(self):
        cmd = b'\x78\x04\x03\x02\x88\x13\x00\x00'
        self.assertEqual(cmd, lcapi.net.cmd.join_receive_delay_1(5000))

    def test_cmd_join_receive_delay_2(self):
        cmd = b'\x78\x04\x03\x03\x70\x17\x00\x00'
        self.assertEqual(cmd, lcapi.net.cmd.join_receive_delay_2(6000))

    def test_cmd_receive_delay_1(self):
        cmd = b'\x78\x04\x03\x04\x88\x13\x00\x00'
        self.assertEqual(cmd, lcapi.net.cmd.receive_delay_1(5000))

    def test_cmd_receive_delay_2(self):
        cmd = b'\x78\x04\x03\x05\x70\x17\x00\x00'
        self.assertEqual(cmd, lcapi.net.cmd.receive_delay_2(6000))

    def test_cmd_datarate(self):
        cmd = b'\x78\x01\x03\x06\x05'
        self.assertEqual(cmd, lcapi.net.cmd.datarate(0x05))

    def test_cmd_rx2_channel(self):
        cmd = b'\x78\x05\x03\x07\x07\xC0\xCa\x89\x36'
        self.assertEqual(cmd, lcapi.net.cmd.rx2_channel(0x07, 915000000))

    def test_cmd_pnm(self):
        cmd = b'\x78\x01\x03\x08\x01'
        self.assertEqual(cmd, lcapi.net.cmd.pnm(0x01))

    def test_cmd_tx_power(self):
        cmd = b'\x78\x01\x03\x09\x04'
        self.assertEqual(cmd, lcapi.net.cmd.tx_power(0x04))

    def test_cmd_channel_mask(self):
        cmd = b'\x78\x09\x03\x0A\x08\xFF\x00\x00\x00\x00\x00\x00\xFF'
        self.assertEqual(
            cmd,
            lcapi.net.cmd.channel_mask(b'\xFF\x00\x00\x00\x00\x00\x00\xFF'))


class TestLcapiNetResponse(unittest.TestCase):
    def test_rsp_adr(self):
        rsp = b'\x78\x02\x03\x00\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_class(self):
        rsp = b'\x78\x02\x03\x01\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_join_receive_delay_1(self):
        rsp = b'\x78\x02\x03\x02\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_join_receive_delay_2(self):
        rsp = b'\x78\x02\x03\x03\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_receive_delay_1(self):
        rsp = b'\x78\x02\x03\x04\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_receive_delay_2(self):
        rsp = b'\x78\x02\x03\x05\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_datarate(self):
        rsp = b'\x78\x02\x03\x06\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_rx2_channel(self):
        rsp = b'\x78\x02\x03\x07\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_pnm(self):
        rsp = b'\x78\x02\x03\x08\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_tx_power(self):
        rsp = b'\x78\x02\x03\x09\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])

    def test_rsp_channel_mask(self):
        rsp = b'\x78\x02\x03\x0A\x00\x00'
        obj, n = from_binary(rsp)
        self.assertTrue(check_rsp_evt_header(obj, rsp))
        self.assertEqual(0, obj['payload']['result'])


if __name__ == "__main__":
    unittest.main()
