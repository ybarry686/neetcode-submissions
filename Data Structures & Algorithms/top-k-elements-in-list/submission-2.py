from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums) 
        sorted_nums = [(count, num) for num, count in counted_nums.items()] 
        heap = []

        # adding to heap; only need to keep heap size to k
        for item in sorted_nums:
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # unpack heap and store in list for output
        res = []
        for i in range(k):
            item = heapq.heappop(heap)
            res.append(item[1])

        return res