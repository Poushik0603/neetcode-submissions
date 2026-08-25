class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        startprice = prices[0]
        n = len(prices)
        for price in prices:
            if price < startprice:
                startprice = price
            else:
                if result < (price - startprice):
                    result = price - startprice
        return result