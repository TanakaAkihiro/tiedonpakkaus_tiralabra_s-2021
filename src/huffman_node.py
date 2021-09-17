class HuffmanNode:
    '''Class for building a Huffman tree.

    Attributes
    ----------
        character: each leaf of the tree has a unique character
        frequency: integer that shows the frequency of its or its children's occurrence
        left: object of its left child node
        right: object of its right child node
    
    '''
    def __init__(self, character, frequency, left=None, right=None):
        self.__character = character
        self.__frequency = frequency
        self.__left = left
        self.__right = right

    @property
    def get_character(self):
        return self.__character
    
    @property
    def get_frequency(self):
        return self.__frequency

    @property
    def get_left_node(self):
        return self.__left
    
    @property
    def get_right_node(self):
        return self.__right
