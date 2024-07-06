class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        r1 = [1]
        r2 = [1, 1]
        answer = [r1, r2]

        if numRows == 1:
            return [r1]
        if numRows == 2:
            return [r1, r2]

        for i in range(3, numRows+1):
            prev_arr = answer[-1]
            arr = [1]
            for i in range(i-2):
                arr.append(prev_arr[i] + prev_arr[i+1])
            arr.append(1)
            answer.append(arr)

        return answer



