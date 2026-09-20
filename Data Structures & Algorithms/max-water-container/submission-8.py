class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_index, r_index = 0, len(heights) - 1
        max_area = float('-inf')

        while l_index < r_index:
            l_val, r_val = heights[l_index], heights[r_index]
            
            length = min(l_val, r_val)
            width = r_index - l_index

            curr_area = length * width
            max_area = max(curr_area, max_area)

            if l_val <= r_val:
                l_index += 1
            
            else:
                r_index -= 1

        return max_area 