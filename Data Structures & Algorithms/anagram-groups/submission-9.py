from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            letters = [0] * 26 # 26 letters in alphabet

            for letter in  word.lower():
                letter_pos = ord(letter) - 97
                letters[letter_pos] += 1
                letters_tup = tuple(letters)

            if not word:
                anagrams[tuple(letters)].append(word)
                continue
            
            anagrams[letters_tup].append(word)
        
        return list(anagrams.values())


