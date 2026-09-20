class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for item in nums:
            if item in sett:
                return True
            sett.add(item)
        return False