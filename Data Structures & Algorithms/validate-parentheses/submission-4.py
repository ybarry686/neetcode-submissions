class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        
        for letter in s:
            if letter in "([{":
                stack.append(letter)
            elif letter == ")": 
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif letter == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif letter == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
        return not stack 

"""
 s = "[]"
 1. letter = "[", stack = ["["]
 2. letter = "]", stack =
"""