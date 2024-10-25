class Solution:
    def maxSubArray(self, nums):
        # 초기값 설정
        maxAnswer = answer = nums[0]

        # 첫 번째 요소 이후부터 시작
        for i in range(1, len(nums)):
            # answer를 현재 요소와 비교해 업데이트
            answer = max(nums[i], answer + nums[i])
            # 최대값 업데이트
            maxAnswer = max(answer, maxAnswer)
                    
        return maxAnswer
