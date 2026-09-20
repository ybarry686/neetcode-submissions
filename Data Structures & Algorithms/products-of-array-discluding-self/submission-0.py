class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_index = float('-inf')
        product = 1

        # case 1:
        # - Multiple Zeros
        #   - Immediately return list of all zeros

        # case 2:
        # - One Zero
        #   - Get product for array of everything but that and place
        #     at that index, zero for everything else

        # case 3:
        # - No Zeros
        #   - Get product of array and divide for each position as you 
        #     iterate through

        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = index
                continue
            
            product *= num
            
        
        # handle 2 or more zeros
        if zero_count > 1:
            res = [0] * len(nums) # return array full of zeros
            return res 

        # handle 1 zero
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = product
            return res
        
        # handle no zeros
        res = []
        for num in nums:
            curr_product = product // num
            res.append(curr_product)
        
        return res







