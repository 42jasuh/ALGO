class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        answer = []
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair not in dic:
                dic[nums[i]] = i
            elif pair in dic:
                answer = [i, dic[pair]]
        return sorted(answer)

            
        