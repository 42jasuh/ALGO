class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        answer = []
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1

        sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        
        if k == 0:
            return []

        for key, value in sorted_dict.items():
            if k == 0:
                break
            answer.append(key)
            k -= 1

        return answer