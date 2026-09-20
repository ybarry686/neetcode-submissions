class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for key, value in enumerate(nums):
            if value in my_dict.values():
                return True
            my_dict[key] = value
        return False