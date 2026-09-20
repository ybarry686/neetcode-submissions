class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for value in s:
            if value in countS:
                countS[value] += 1
            else:
                countS[value] = 1
        
        for value in t:
            if value in countT:
                countT[value] += 1
            else:
                countT[value] = 1     
        
        return countS == countT