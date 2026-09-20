class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_seq = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
            
            seen[s[right]] = right
            longest_seq = max((right - left) + 1, longest_seq)

        return longest_seq        
