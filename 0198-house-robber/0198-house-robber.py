class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0]*(length+1)
        dp[1] = nums[0]

        if length >= 2:
            dp[2] = max(dp[1], nums[1])
        
        if length >= 3:
            for i in range(3, length+1):
                dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        
        return dp[length]
        