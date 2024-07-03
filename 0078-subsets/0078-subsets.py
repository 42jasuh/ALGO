class Solution:
    def subsets(self, nums):
        answer = []
        self.backtrack(nums, 0, [], answer)
        return answer

    def backtrack(self, nums, start, subset, answer):
        answer.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtrack(nums, i + 1, subset, answer)
            subset.pop()
