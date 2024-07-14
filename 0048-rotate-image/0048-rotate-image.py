class Solution:
    def helper(self, n: int, original: List[List[int]]) -> List[int]:
        arr = []
        for i in range(n):
            row = []
            for k in range(n-1,-1,-1):
                row.append(original[k][i])
            arr.append(row)
        original[:] = arr
        return original

    def rotate(self, matrix: List[List[int]]) -> None:        
        n = len(matrix)
        return self.helper(n, matrix)
