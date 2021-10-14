import os

class LZ77:
    '''Implementation of LZ77 algorithm.

    Attributes
    ----------
        sb_size: search buffer size
        lab_size: look ahead buffer size 
    '''
    def __init__(self, path):
        self.__path = path
        self.__sb_size = 512
        self.__lab_size = 15

    def search_best_match(self, text, index):
        match_offset = -1
        match_length = -1

        for i in range(3, self.__lab_size):
            if index + i > len(text):
                break
            read_pointer = max(0, index - self.__sb_size)
            sub_string = text[index:index + i]

            for j in range(read_pointer, index):
                if j + i <= len(text):
                    string = text[j:j+i]
                if sub_string == string and len(sub_string) > match_length:
                    match_length = len(sub_string)
                    match_offset = index - j
                

        if match_length == -1:
            return None
        return (match_offset, match_length)
    
    def encode_text(self, text):
        index = 0
        result = ""
        while index < len(text):
            match = self.search_best_match(text, index)

            if match:
                offset = format(match[0], "b")
                length = format(match[1], "b")
                result = result + "1" + offset.rjust(12, '0') + length.rjust(4,'0')
                index += match[1]
            
            else:
                symbol = format(ord(text[index]), "b")
                result = result + "0" + symbol.rjust(8, '0')
                index += 1
        return result

    def pad_binary_code(self, code):
        '''Pad the encoded text's length in order to make it divisible by 8.

        Args
        ----
            code: encoded text

        Returns
        -------
            bytearray(byte_list): list of numbers that were converted from binary numbers
        '''
        pad_amount = 0
        while len(code) % 8 != 0:
            code += "0"
            pad_amount += 1
        self.__padding = pad_amount
        division = []
        length = len(code)
        for i in range(0, length//8):
            division.append(code[i*8:(i*8) + 8])
        byte_list = []
        for i in division:
            byte_list.append(int(i, 2))
        return bytearray(byte_list)

    
    def compress(self):
        with open(self.__path) as file:
            text = file.read()
            binary_code = self.encode_text(text)
            binary_code = self.pad_binary_code(binary_code)
        
        compressed_file = os.path.splitext(self.__path)[0]+".bin" 
        with open(compressed_file, "wb") as file:
            file.write(binary_code)
        
        return os.path.getsize(compressed_file)