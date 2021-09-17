import unittest
from huffman_node import HuffmanNode

class TestHuffmanNode(unittest.TestCase):
    def setUp(self):
        self.node = HuffmanNode("a", 10)
    
    def test_get_character(self):
        self.assertEqual(self.node.get_character, "a")