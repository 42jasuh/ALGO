class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        f, s = 0, 0        
        length = len(nums)
        while f < length and s < length:
            if nums[f] != 0 and nums[s] == 0 and s < f:
                nums[f], nums[s] = nums[s], nums[f]
            elif f < s and nums[s] == 0 and nums[f] != 0:                
                f += 1
            if nums[f] == 0:
                f += 1
            if nums[s] != 0:
                s += 1
        return nums

        
        
        