class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0        
        length = len(prices)
        for i in range(length):
            if prices[i] < prices[index]:
                index = i
        index2 = index                
        for i in range(index, length):
            if prices[i] > prices[index2]:
                index2 = i
        # print(f'index: {index} index2: {index2}')
        if index != index2:
            return prices[index2] - prices[index]
        return 0
        