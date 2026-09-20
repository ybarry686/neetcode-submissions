class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char in "{[(":
                my_stack.append(char)
                continue

            if char in "}])" and not my_stack:
                return False
            
            else:
                opening_char = my_stack.pop()
                
                if char == "}" and opening_char != "{":
                    return False
                
                if char == "]" and opening_char != "[":
                    return False
                
                if char == ")" and opening_char != "(":
                    return False 
                
        
        return len(my_stack) == 0
