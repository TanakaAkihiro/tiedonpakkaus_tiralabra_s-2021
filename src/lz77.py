class LZ77:
    '''Implementation of LZ77 algorithm.

    Attributes
    ----------
        sb_size: search buffer size
        lab_size: look ahead buffer size 
    '''
    def __init__(self):
        self.__sb_size = 512
        self.__lab_size = 15

    def search_best_match(self, text, index):
        match_offset = -1
        match_length = -1

        for i in range(3, self.__lab_size):
            read_pointer = max(0, index - self.__sb_size)
            sub_string = text[index:index + i]

            for j in range(read_pointer, index):
                if sub_string == text[read_pointer:j] and len(sub_string) > match_length:
                    match_length = len(sub_string)
                    match_offset = index - i

        if match_length == -1:
            return None
        return (match_offset, match_length)