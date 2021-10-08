from config import FILE_PATH
from huffman_coding import HuffmanCoding
import time

huffman = HuffmanCoding(FILE_PATH)

start = time.time()
compressed = huffman.compress()
end = time.time()

print("Huffmanin koodauksen pakkaaminen: " + str((end - start) * 1000) + "ms")

start = time.time()
decompressed = huffman.decompress()
end = time.time()

print("Huffmanin koodauksen purkaminen: " + str((end - start) * 1000) + "ms")
print()
print("Tiedoston koko: " + str(decompressed/1000) + "kt")
print("Tiedoston koko pakattuna Huffmanin koodauksella: " + str(compressed/1000) + "kt")