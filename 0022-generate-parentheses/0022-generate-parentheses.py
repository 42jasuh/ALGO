class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(text, opening, closing):
            if opening > n or closing > n:
                return
            if opening < closing:
                return
            if opening == n and closing == n:
                answer.append(text)
            dfs(text+'(', opening + 1, closing)
            dfs(text+')', opening, closing+1)
        
        dfs("", 0, 0)
        
        return answer