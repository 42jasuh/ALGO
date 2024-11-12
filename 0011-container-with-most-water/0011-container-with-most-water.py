class Solution:
    def maxArea(self, height: List[int]) -> int:
        def S(l, r, height):
            return (r-l) * min(height[l], height[r])

        length = len(height)
        cur_s = S(0, length-1, height)
        
        for i in range(length-1):
            for j in range(i+1, length):
                s = S(i, j, height)
                if cur_s < s:
                    cur_s = s
        return cur_s            
