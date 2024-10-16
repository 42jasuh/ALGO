class Solution:
    def isValid(self, s: str) -> bool:
        dic_2 = {')': 1, '}': 1, ']': 1}
        stack = []
        for alpha in s:
            stack.append(alpha)
            try:
                if alpha in dic_2 and stack != []:
                    if alpha == ')' and stack[-2] == '(':
                        stack.pop()
                        stack.pop()
                    elif alpha == '}' and stack[-2] == '{':
                        stack.pop()
                        stack.pop()
                    elif alpha == ']' and stack[-2] == '[':
                        stack.pop()
                        stack.pop()
            except:
                pass
        if stack == []:
            return True
        return False
                
                    

