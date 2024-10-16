class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = max((r-l) * min(height[l], height[r]), 0)
        while l < r:
            area = max(area, (r-l)*min(height[r],height[l]))
            L, R = height[l], height[r]            
            if L <= R:
                l += 1
            else:
                r -= 1
        return area


