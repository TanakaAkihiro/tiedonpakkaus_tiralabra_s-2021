import unittest
from huffman_coding import HuffmanCoding
from huffman_node import HuffmanNode


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman_coding = HuffmanCoding("test.txt")

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
        left = HuffmanNode("a", 1)
        right = HuffmanNode("b", 2)
        node = HuffmanNode(None, 3, left, right)
        self.huffman_coding.create_binary_codes(node, "")
        self.assertEqual(self.huffman_coding.get_encoding_binary_codes, {
                         "a": "0", "b": "1"})

    def test_encode_text(self):
        left = HuffmanNode("a", 1)
        right = HuffmanNode("b", 2)
        node = HuffmanNode(None, 3, left, right)
        self.huffman_coding.create_binary_codes(node, "")
        self.assertEqual(self.huffman_coding.encode_text("abb"), "011")

    def test_decode_text(self):
        left = HuffmanNode("a", 1)
        right = HuffmanNode("b", 2)
        node = HuffmanNode(None, 3, left, right)
        self.huffman_coding.create_binary_codes(node, "")
        self.assertEqual(self.huffman_coding.decode_text("011"), "abb")
