from config import FILE_PATH
from huffman_coding import HuffmanCoding

huffman = HuffmanCoding(FILE_PATH)

huffman.compress()
huffman.decompress()
