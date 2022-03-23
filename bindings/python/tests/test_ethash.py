# ethash: C/C++ implementation of Ethash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

import unittest

import etchash


class TestEtchash(unittest.TestCase):
    epoch_number = 440
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


if __name__ == '__main__':
    unittest.main()
