from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums)
        sorted_nums = [(-count, num) for num, count in counted_nums.items()]
        res = []

        heapq.heapify(sorted_nums)

        while len(res) < k:
            item = heapq.heappop(sorted_nums)
            res.append(item[1])

        return res