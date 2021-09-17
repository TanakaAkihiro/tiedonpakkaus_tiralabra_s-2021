import heapq
from huffman_node import HuffmanNode

class HuffmanCoding:
    def __init__(self, path):
        self.__path = path
        self.__node_heap = []
        self.__encoding_binary_codes = {}
        self.__decoding_binary_codes = {}
    
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
            self.__encoding_binary_codes[node.get_character()] = code
            self.__decoding_binary_codes[code] = node.get_character()
            return
        
        self.create_binary_codes(node.get_left_node(), code+"0")
        self.create_binary_codes(node.get_right_node(), code+"1")

    def encode_text(self, text):
        result = ""
        for char in text:
            result += self.__encoding_binary_codes[char]
        return result

    def decode_text(self, binary_code):
        result = ""
        code = ""
        for i in binary_code:
            code += i
            if code in self.__decoding_binary_codes:
                result += self.__decoding_binary_codes[code]
                code = ""
        return result
    
    def compress(self):
        with open(self.__path) as file:
            text = file.read()
            frequency = self.frequency_dict(text)
            self.order_nodes(frequency)
            self.connect_nodes()
            self.create_binary_codes(heapq.heappop(self.__node_heap), "")
            binary_code = self.encode_text(text)
        
        with open("compressed_"+self.__path, "w") as file:
            file.write(binary_code)

    def decompress(self):
        with open("compressed_" + self.__path) as file:
            binary_code = file.read()
            text = self.decode_text(binary_code)
        with open("decomressed_" + self.__path, "w") as file:
            file.write(text)
