import unittest
from huffman_node import HuffmanNode

class TestHuffmanNode(unittest.TestCase):
    def setUp(self):
        self.node = HuffmanNode("a", 10)
    
    def test_get_character(self):
        self.assertEqual(self.node.get_character, "a")

    def test_get_frequency(self):
        self.assertEqual(self.node.get_frequency, 10)

    def test_get_left_node(self):
        node = HuffmanNode("b", 20, self.node)
        self.assertEqual(node.get_left_node, self.node)

    def test_get_right_node(self):
        node = HuffmanNode("c", 30, None, self.node)
        self.assertEqual(node.get_right_node, self.node)