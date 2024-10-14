class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0]
        answer = nums[0]
        for i in range(1, n):
            if nums[i] > total and total < 0:
                total = nums[i]
            else:
                total += nums[i]
            answer = max(answer, total)
        return answer