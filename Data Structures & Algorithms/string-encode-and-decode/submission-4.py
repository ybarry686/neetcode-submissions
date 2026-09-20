class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_word = str(len(word)) + "#" + word
            encoded_str += encoded_word
        
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []

        while index < len(s):
            # get current strings length
            curr_word_len = ""
            curr_char = s[index]
            
            while curr_char not in "#":
                curr_word_len += curr_char
                index += 1
                curr_char = s[index]

            k = int(curr_word_len)
            decoded_word = ""

            # append each letter into current string
            for i in range(k):
                index += 1
                decoded_word += s[index]
            
            # append current string to output list
            res.append(decoded_word)
            index += 1 # move pointer forward to next word_length

        return res
        
