from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        
        for word in strs:
            count = [0] * 26 # Create an array for all letters 'a-z'

            for letter in word:
                # Find index of letter in array and +1 to value at that position
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count) # key values in dict must be hashable
            anagrams_dict[key].append(word) # append key and value into dict
        
        return list(anagrams_dict.values())
            
