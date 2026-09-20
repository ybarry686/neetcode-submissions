class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        high = float('-inf')
        
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height
            high = max(area, high)

            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
                l += 1        
        return high

    """ 
    height=[1,7,2,5,4,7,3,6] 
    --> L = 0, r = 7, width = 7, height = 1, area = 7, high = 7
    --> L = 1, r = 7, width = 6, height = 6, area = 36, high = 36
    --> L = 1, r = 6, width = 5, height = 3, area = 15, high = 36
    --> L = 1, r = 5, width = 4, height = 7, area = 28, high = 36
    --> L = 2, r = 4, width = 2, height = 2, area = 4, high = 36
    --> L = 3, r = 4, width = 1, height = 4, area = 4, high = 36
    --> loop ends

    """

