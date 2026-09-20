class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:
            left_val = numbers[left_index]
            right_val = numbers[right_index]
            curr_sum = left_val + right_val

            if curr_sum == target:
                return [left_index + 1, right_index + 1]
            
            elif curr_sum > target:
                right_index -= 1
            
            else:
                left_index += 1

        return -1