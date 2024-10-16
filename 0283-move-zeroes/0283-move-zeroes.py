from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1
        for i in range(cnt):
            nums.remove(0)
        for i in range(cnt):
            nums.append(0)
        return nums
