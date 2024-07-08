class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        total = 0
        consecutive = True
        for n in arr:
            if n % 2 == 1:
                total += 1
                consecutive = True                
            else:
                consecutive = False
                total = 0
            if total >= 3 and consecutive:
                return True
        return False