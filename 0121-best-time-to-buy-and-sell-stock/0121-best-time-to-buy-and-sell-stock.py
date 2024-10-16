class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - buy
            if profit < 0:
                buy = prices[i]
            else:
                pre_profit = max(pre_profit, profit)
        return pre_profit       

        