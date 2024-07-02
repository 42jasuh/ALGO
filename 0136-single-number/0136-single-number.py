class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        for k, v in dic.items():
            if v == 1:
                return k
        