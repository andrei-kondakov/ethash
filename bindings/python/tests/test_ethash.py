# ethash: C/C++ implementation of Ethash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

import unittest

import etchash


class TestEtchash(unittest.TestCase):
    epoch_number = 220
    nonce = 0x6e2ef531c5c4a9f4
    header_hash = bytes.fromhex(
        '81568d50e471c14182294fa449b0154077273427214b4a5db31a3262dd21f789')
    mix_hash = bytes.fromhex(
        '930259684a1817329013b074e691fbeb359bf25825697efca646acc2442ab56b')
    final_hash = bytes.fromhex(
        '00000000de434405ebda09d28ed6aa3af1d6eb990e33953aa41aaebd1a46552b')

    def test_keccak(self):
        h256 = ('c5d2460186f7233c927e7db2dcc703c0'
                'e500b653ca82273b7bfad8045d85a470')
        h512 = ('0eab42de4c3ceb9235fc91acffe746b2'
                '9c29a8c366b7c60e4e67c466f36a4304'
                'c00fa9caf9d87976ba469bcbe06713b4'
                '35f091ef2769fb160cdab33d3670680e')

        self.assertEqual(etchash.keccak_256(b'').hex(), h256)
        self.assertEqual(etchash.keccak_512(b'').hex(), h512)

    def test_hash(self):
        f, m = etchash.hash(self.epoch_number, self.header_hash, self.nonce)
        self.assertEqual(m, self.mix_hash)
        self.assertEqual(f, self.final_hash)

    def test_verify(self):
        t = etchash.verify(self.epoch_number, self.header_hash, self.mix_hash, self.nonce,
                           self.final_hash)
        self.assertTrue(t)
        self.assertEqual(type(t), bool)

    def test_hash_2(self):
        shares = [
            (['0x4f29c0e5dc784d8b', '0x32d6c83f7fc493aa224a8fcc3ac007e6113d28ed70717e7d5a7505d72d4bdd7f',
              '0xb27518ae34f7e81c56a4dedb81df93c4d4301d90643678044b3445ded0b331ce'], 14790284),
            (['0xfaa3bac206ea78e8', '0x7f822a499da904d96b7cd128acebfdbc251775bcb0ceb47f277ad0775d3797d6',
              '0x18ea122233b503db51b881d8a8c57121374758028c4be97bafbf9fd2d5bdc8ab'], 14790283),
            (['0x63f852a248ba7e79', '0x4b713ed6ff8033738ff4b20cafd9b851debc14561a9adab53a897d7560e7dc2f',
              '0x885317e46a4dfa12f41e30a35e05700fa8c0df32fe0e456fb3bc8cf5b4b7dd25'], 14790280),
            (['0x00cb38a4501514a7', '0x9786b0d8d9a9d909d5f5e3458bce92f274f99231e92591ccab4a010a94c5022f',
              '0x7a14ab63e2403e8228951a85ce0ce1e925f30c145cde660429af3b98d7e36b40'], 14790000),
            (['0x8cd620f7f0c3782d', '0x7d0be9b58d500800ec240dffc341f76585dedf3886ada307bdf43f12e462b17a',
              '0xa4e7d216c54a4e96a5e8b0bcd08931647d3db27dd445a01e58aafb71ad80a9b0'], 14760000),
        ]
        for params, height in shares:
            f, m = etchash.hash(height // 60_000, bytes.fromhex(params[1][2:]), int(params[0], 16))
            self.assertEqual(m.hex(), params[2][2:])


if __name__ == '__main__':
    unittest.main()
