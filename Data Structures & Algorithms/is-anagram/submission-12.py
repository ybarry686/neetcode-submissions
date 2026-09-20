class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. Brute Force: One solution is to sort the string and compare them
        --> Time Complexity: O(n logn)
        --> Space Complexity: O(1)
        2. Optimized: Store all values for both strings in two separate hashmaps; compare them
        --> Time Complexity: O(n)
        --> Space Complexity: O(n), since we are adding all input values into hashmaps 
        """
        if len(s) != len(t):
            return False # anagrams are of the same length
        # {b: 1, c: 1}
        seen_s = {}
        seen_t = {}
        for value in s:
            if value in seen_s:
                seen_s[value] += 1
            else:
                seen_s[value] = 1
        for value in t:
            if value in seen_t:
                seen_t[value] += 1
            else:
                seen_t[value] = 1
        return seen_s == seen_t