# ethash: C/C++ implementation of Ethash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

import unittest

import ubqhash

# 2893974
# ['0xe4d90fc8f41abb75', '0x16b1595978d442e24e3ae2e919c11c7a6b40dc30e628aa20362bcade8853a766', '0xf6f023da17cd7381e76e924a39d1cb064586ff98683337e0d9aff6d3994caed6']
# b'\x00\x00\x00\x00\xd1\xbej\xd4\xa1_\xc3\xe1D\xaf=\xd5(\xb7)6:}\xd3\x18\xc8\xa6}\x8d\xf5\xa3\xfc\x1a'

# 2904640
# '0x258dfc351b37441f', '0xf2d723c43b2535c012e4ee5377f3276e9d568e823b44e2b7f9e8b3fdb78cea0a', '0xaa0647a72ee211c29d4929d30a9f1a30504c35469086a080927b51bfcd8bc8f4'
# b'\x00\x00\x00\x01a\xe5\x99\x82\xadX\x1eJ\x99\x8duh\xc7\xeb\xb6\x96\x81\x1f>\x99m\xea`\x07$\xc3\x14\xd7'


class TestUbqhash(unittest.TestCase):
    epoch_number = 96
    nonce = 0x258dfc351b37441f
    header_hash = bytes.fromhex(
        'f2d723c43b2535c012e4ee5377f3276e9d568e823b44e2b7f9e8b3fdb78cea0a')
    mix_hash = bytes.fromhex(
        'aa0647a72ee211c29d4929d30a9f1a30504c35469086a080927b51bfcd8bc8f4')
    final_hash = bytes.fromhex(
        '0000000161e59982ad581e4a998d7568c7ebb696811f3e996dea600724c314d7')

    def test_keccak(self):
        h256 = ('c5d2460186f7233c927e7db2dcc703c0'
                'e500b653ca82273b7bfad8045d85a470')
        h512 = ('0eab42de4c3ceb9235fc91acffe746b2'
                '9c29a8c366b7c60e4e67c466f36a4304'
                'c00fa9caf9d87976ba469bcbe06713b4'
                '35f091ef2769fb160cdab33d3670680e')

        self.assertEqual(ubqhash.keccak_256(b'').hex(), h256)
        self.assertEqual(ubqhash.keccak_512(b'').hex(), h512)

    def test_hash(self):
        f, m = ubqhash.hash(self.epoch_number, self.header_hash, self.nonce)
        self.assertEqual(m, self.mix_hash)
        self.assertEqual(f, self.final_hash)

    def test_verify(self):
        t = ubqhash.verify(self.epoch_number, self.header_hash, self.mix_hash, self.nonce,
                          self.final_hash)
        self.assertTrue(t)
        self.assertEqual(type(t), bool)


if __name__ == '__main__':
    unittest.main()
