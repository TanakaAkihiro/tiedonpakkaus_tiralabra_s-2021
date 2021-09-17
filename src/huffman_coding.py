import heapq
from huffman_node import HuffmanNode

class HuffmanCoding:
    def __init__(self, path):
        self.__path = path
        self.__node_heap = []
        self.__binary_codes = {}
    
    def frequency_dict(self, text):
        frequency = {}
        for i in text:
            if not i in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        return frequency
    
    def order_nodes(self, frequency):
        for i, j in frequency.items():
            node = HuffmanNode(i, j)
            heapq.heappush(self.__node_heap, (j, node))
    
    def connect_nodes(self):
        while len(self.__node_heap) > 1:
            left_node = heapq.heappop(self.__node_heap)
            right_node = heapq.heappop(self.__node_heap)
            new_frequency = left_node.get_frequency() + right_node.get_frequency()
            new_node = HuffmanNode(None, new_frequency, left_node, right_node)
            heapq.heappush(self.__node_heap, new_node)
    
    def create_binary_codes(self, node, code):
        if node.get_left_node() is None and node.get_right_node() is None:
            self.__binary_codes[node.get_character()] = code
            return
        
        self.create_binary_codes(node.get_left_node(), code+"0")
        self.create_binary_codes(node.get_right_node(), code+"1")
