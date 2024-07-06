import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        min_value = math.ceil(length / 2)
        nums.sort()

        if length == 1:
            return nums[0]

        count_1= 1
        max_val = float("-inf")
        real_val = None

        for i in range(length-1):
            current_val, next_val = nums[i], nums[i+1]

            if current_val == next_val:
                count_1 += 1
                if max_val < count_1:
                    real_val = current_val
                    max_val = count_1
            else:
                if max_val < count_1:
                    max_val = count_1
                    real_val = current_val
                count_1 = 1
        
        if max_val >= min_value:
            return real_val
        return

            
