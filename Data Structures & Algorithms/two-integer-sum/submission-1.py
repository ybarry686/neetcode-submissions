class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        result = []
        for index, value in enumerate(nums):
            complement = target - value
            if complement in my_dict:
                result.append(my_dict[complement])
                result.append(index)
                return result
            my_dict[value] = index
        return result