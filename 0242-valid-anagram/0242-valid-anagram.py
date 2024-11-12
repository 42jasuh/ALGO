class Solution:
    def isAnagram(self, s,t):
        dic1 = {}
        dic2 = {}
        for c in s:
            if c not in dic1:
                dic1[c] = 1
            else:
                dic1[c] += 1                
        for c in t:
            if c not in dic2:
                dic2[c] = 1
            else:
                dic2[c] += 1        
        if dic1==dic2:
            return True
        return False