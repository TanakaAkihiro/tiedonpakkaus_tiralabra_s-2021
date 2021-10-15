from config import FILE_PATH
from huffman_coding import HuffmanCoding
from lz77 import LZ77
import time

huffman = HuffmanCoding(FILE_PATH)
lz77 = LZ77(FILE_PATH)

while True:
    select = input("1 - Huffmanin koodaus\n2 - LZ77-algoritmi\n3 - Lopeta\n---------------------\n")

    start = time.time()
    if select == "1":
        compressed = huffman.compress()
    elif select == "2":
        compressed = lz77.compress()
    elif select == "3":
        break
    else:
        print("Virheellinen syöte")
        print("------------------")
        continue
    end = time.time()

    if select == "1":
        print("Huffmanin koodauksen pakkaaminen: " + str((end - start) * 1000) + "ms")
    else:
        print("LZ77-algoritmin pakkaaminen: " + str((end - start) * 1000) + "ms")

    start = time.time()
    if select == "1":
        decompressed = huffman.decompress()
    else:
        decompressed = lz77.decompress()
    end = time.time()

    if select == "1":
        print("Huffmanin koodauksen purkaminen: " + str((end - start) * 1000) + "ms")
    else:
        print("LZ77-algoritmin purkaaminen: " + str((end - start) * 1000) + "ms")
    print()
    print("Tiedoston koko: " + str(decompressed/1000) + "kt")
    print("Tiedoston koko pakattuna Huffmanin koodauksella: " + str(compressed/1000) + "kt")