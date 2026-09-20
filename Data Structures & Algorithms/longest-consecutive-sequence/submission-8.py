class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute Force:
            - Sort array elements
            - max_count and curr_count
            - increment curr_count while i >= i-1
            - return max_count

        '''
        seen = set(nums)
        longest_seq = 0

        for num in nums:
            curr_seq = 0
            curr_num = num
            
            # not start of sequence
            if curr_num - 1 in seen:
                continue

            # start of sequence, continue until sequence ends
            while curr_num in seen:
                curr_seq += 1
                curr_num += 1

            longest_seq = max(curr_seq, longest_seq) 

        return longest_seq