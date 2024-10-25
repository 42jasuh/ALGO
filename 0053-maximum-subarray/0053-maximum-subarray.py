class Solution:
    def maxSubArray(self, nums):
        answer = nums[0]
        maxAnswer = nums[0]
        length = len(nums)

        if length >= 2:
            for i in range(1, length):
                if answer < 0 and answer < nums[i]:
                    answer = nums[i]
                else:
                    answer = answer+nums[i]
                maxAnswer = max(answer, maxAnswer)
                    
        return maxAnswer   