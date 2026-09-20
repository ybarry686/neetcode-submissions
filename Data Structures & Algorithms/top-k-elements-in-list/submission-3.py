from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # creating frequency map
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # adding values to bucket list
        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for bucket in freq[::-1]:
            for num in bucket:
                res.append(num)
                
                if len(res) >= k:
                    return res
        
        return res
            
    