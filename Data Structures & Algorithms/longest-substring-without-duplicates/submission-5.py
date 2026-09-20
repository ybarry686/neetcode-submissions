class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        unique = set()
        
        while right < len(s):
            left_val = s[left]
            right_val = s[right]

            if right_val not in unique:
               unique.add(right_val)
               right += 1
            else:
                # longest = max(len(unique), longest)
                unique.remove(left_val)
                left += 1
            longest = max(len(unique), longest)
        return longest
