import unittest
from huffman_coding import HuffmanCoding
from config import FILE_PATH

class FakeHuffmanNode:
    def __init__(self, character, frequency, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    @property
    def get_character(self):
        return self.character

    @property
    def get_frequency(self):
        return self.frequency

    @property
    def get_left_node(self):
        return self.left

    @property
    def get_right_node(self):
        return self.right


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman_coding = HuffmanCoding(FILE_PATH)

        self.left_node = FakeHuffmanNode("a", 1)
        self.right_node = FakeHuffmanNode("b", 2)
        self.root = FakeHuffmanNode(None, 3, self.left_node, self.right_node)

    def test_get_frequency_dict(self):
        dictionary = self.huffman_coding.frequency_dict("aa")
        self.assertEqual(dictionary, {"a": 2})

    def test_order_nodes(self):
        self.huffman_coding.order_nodes({"a": 2})
        self.assertEqual(len(self.huffman_coding.get_node_heap), 1)

    def test_connect_nodes(self):
        self.huffman_coding.order_nodes({"a": 2, "b": 1})
        self.huffman_coding.connect_nodes()
        self.assertEqual(len(self.huffman_coding.get_node_heap), 1)

    def test_create_binary_codes(self):
        self.huffman_coding.create_binary_codes(self.root, "")
        self.assertEqual(self.huffman_coding.get_encoding_binary_codes, {
                         "a": "0", "b": "1"})

    def test_encode_dictionary(self):
        self.huffman_coding.create_binary_codes(self.root, "")
        self.assertEqual(self.huffman_coding.encode_dictionary(), "00000000101000000111101100100010011000010010001000111010001000000010001000110000001000100010110000100000001000100110001000100010001110100010000000100010001100010010001001111101")

    def test_encode_text(self):
        self.huffman_coding.create_binary_codes(self.root, "")
        self.assertEqual(self.huffman_coding.encode_text("abb"), "011")

    def test_decode_text(self):
        self.huffman_coding.create_binary_codes(self.root, "")
        self.assertEqual(self.huffman_coding.decode_text("00000000101000000111101100100010011000010010001000111010001000000010001000110000001000100010110000100000001000100110001000100010001110100010000000100010001100010010001001111101011"), "abb")

    def test_compress(self):
        self.assertEqual(self.huffman_coding.compress(), 441)
    
    def test_decompress(self):
        self.assertEqual(self.huffman_coding.decompress(), 57)