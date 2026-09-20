class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            store hashmap of letters we've seen along with their counts
            while looping through the array: update counts and if the new count 
        """
        left = 0
        count = {}
        longest_seq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            longest_seq = max(longest_seq, (right - left + 1))

        return longest_seq
        
            


