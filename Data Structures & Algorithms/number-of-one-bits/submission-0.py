class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in str(bin(n)[2:]):
            if int(i) == 1:
                count += 1
        return count

