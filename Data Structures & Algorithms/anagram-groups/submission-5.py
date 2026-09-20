from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26 # Create array for all letters from 'a-z'
            for letter in word:
                # Find index of letter in array and add 1 to it
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count) # Key valeus in dict must be hashable
            res[key].append(word) # Append key and value into dict
            print(res.values())
        
        return list(res.values())
