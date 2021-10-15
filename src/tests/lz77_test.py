import unittest
from lz77 import LZ77
from config import FILE_PATH


class TestLZ77(unittest.TestCase):
    def setUp(self):
        self.lz = LZ77(FILE_PATH)

    def test_search_best_match(self):
        self.assertEqual(self.lz.search_best_match("ababa", 2), (2, 3))
    
    def test_encode_text(self):
        self.assertEqual(self.lz.encode_text("ababa"), "0011000010011000101000000100011")
    
    def test_pad_binary_code(self):
        self.assertEqual(self.lz.pad_binary_code("0011000010011000101000000100011"), bytearray(b'0\x98\xa0F'))

    def test_decode_byte_code(self):
        self.assertEqual(self.lz.decode_byte_code(bytearray(b'0\x98\xa0F')), "00110000100110001010000001000110")

    def test_decode_text(self):
        self.assertEqual(self.lz.decode_text("00110000100110001010000001000110"), "ababa")

    
    def test_compress(self):
        self.assertEqual(self.lz.compress(), 36)
    
    def test_decompress(self):
        self.assertEqual(self.lz.decompress(), 57)

    