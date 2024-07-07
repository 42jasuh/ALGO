class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles

        # 음료수를 마신다
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            # 빈병을 음료수로 바꾼다
            refillBottles = emptyBottles // numExchange

            # 마신 음료수를 더한다
            total += refillBottles

            # 빈 병의 개수를 조정한다
            emptyBottles -= refillBottles * numExchange
            emptyBottles += refillBottles

        return total
