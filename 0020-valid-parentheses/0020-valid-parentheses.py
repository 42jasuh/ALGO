class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for i in range(1, len(s)):
            if stack and s[i] in bracket_map and bracket_map[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        if stack == []:
            return True
        return False