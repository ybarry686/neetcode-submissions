class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        s = s.lower()

        while l <= r:
            l_char, r_char = s[l], s[r]
            print(l_char, r_char)
            if not self._is_alphanumeric(l_char):
                l += 1
            
            if not self._is_alphanumeric(r_char):
                r -= 1
            
            if self._is_alphanumeric(l_char) and self._is_alphanumeric(r_char):
                if l_char != r_char:
                    return False
                
                else:
                    l += 1
                    r -= 1

        return True


    def _is_alphanumeric(self, char: str) -> bool:
        return char.isalnum()

