import heapq
from huffman_node import HuffmanNode


class HuffmanCoding:
    '''Class for Huffman coding.

    Attributes
    ----------
        path: path for the file that will be compressed/decompressed
        node_heap: binary heap for ordering the characters that shows up in the file by their occurrences
        encoding_binary_codes: dictionary for new binary codes for the used characters
        decoding_binary_codes: dictionary for decoding compressed file
    '''

    def __init__(self, path):
        self.__path = path
        self.__node_heap = []
        self.__encoding_binary_codes = {}
        self.__decoding_binary_codes = {}

    def frequency_dict(self, text):
        '''Create a frequency dictionary.

        Returns
        -------
            dictionary of characters' frequencies
        '''
        frequency = {}
        for i in text:
            if not i in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        return frequency

    def order_nodes(self, frequency):
        '''Order nodes by the frequency of its character in order to build a Huffman tree.
        These nodes are the leaves of the Huffman tree.
        '''
        for i, j in frequency.items():
            node = HuffmanNode(i, j)
            heapq.heappush(self.__node_heap,
                           (node.get_frequency, id(node), node))

    def connect_nodes(self):
        '''Connect the ordered nodes.
        '''
        while len(self.__node_heap) > 1:
            left_node = heapq.heappop(self.__node_heap)[2]
            right_node = heapq.heappop(self.__node_heap)[2]
            new_frequency = left_node.get_frequency + right_node.get_frequency
            new_node = HuffmanNode(None, new_frequency, left_node, right_node)
            heapq.heappush(self.__node_heap,
                           (new_node.get_frequency, id(new_node), new_node))

    @property
    def get_node_heap(self):
        '''Method for testing two previous methods

        Returns
        -------
            node_heap: heap of nodes
        '''
        return self.__node_heap

    def create_binary_codes(self, node, code):
        '''Set binary codes for each character based on their frequency.
        '''
        if node.get_left_node is None and node.get_right_node is None:
            self.__encoding_binary_codes[node.get_character] = code
            self.__decoding_binary_codes[code] = node.get_character
            return

        self.create_binary_codes(node.get_left_node, code+"0")
        self.create_binary_codes(node.get_right_node, code+"1")
    
    @property
    def get_encoding_binary_codes(self):
        '''Method for testing the previous method

        Returns
        -------
            encoding_binary_codes: dictionary to convert text to binary code
        '''
        return self.__encoding_binary_codes

    def encode_text(self, text):
        '''Rewrite the given text with the created binary codes.

        Returns
        -------
            result: compressed text
        '''
        result = ""
        for char in text:
            result += self.__encoding_binary_codes[char]
        return result

    def decode_text(self, binary_code):
        '''Rewrite the given binary codes to its original form.

        Returns
        -------
            result: original text
        '''
        result = ""
        code = ""
        for i in binary_code:
            code += i
            if code in self.__decoding_binary_codes:
                result += self.__decoding_binary_codes[code]
                code = ""
        return result

    def compress(self):
        '''Compress the given file and rewrite it with the created binary codes on new file.
        '''
        with open(self.__path) as file:
            text = file.read()
            frequency = self.frequency_dict(text)
            self.order_nodes(frequency)
            self.connect_nodes()
            self.create_binary_codes(heapq.heappop(self.__node_heap)[2], "")
            binary_code = self.encode_text(text)

        with open("files/compressed.txt", "w") as file:
            file.write(binary_code)

    def decompress(self):
        '''Decompress the given file.
        '''
        with open("files/compressed.txt") as file:
            binary_code = file.read()
            text = self.decode_text(binary_code)
        with open("files/decompressed.txt", "w") as file:
            file.write(text)
