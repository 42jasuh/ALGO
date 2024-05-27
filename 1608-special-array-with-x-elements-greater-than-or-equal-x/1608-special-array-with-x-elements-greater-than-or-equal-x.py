class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        start = nums[0]
        increase_flag = False

        while True:
            cnt = 0
            for val in nums:
                if start <= val:
                    cnt += 1
            if start == cnt:
                return start
            if start < cnt:
                increase_flag = True
                start += 1
            elif start > cnt:
                if increase_flag is True:
                    return -1
                start -= 1