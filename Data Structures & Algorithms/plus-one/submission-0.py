class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        arr = []
        for item in digits:
            s += str(item)
        value = int(s) + 1

        for num in str(value):
            arr.append(int(num))
        
        return arr