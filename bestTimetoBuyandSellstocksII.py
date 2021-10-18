from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0
        
        profit = 0
        curr = prices[0]
        
        for i in (prices[1:]) :
            if i  >= curr :
                profit = profit + (i - curr)
                curr = i
            else :
                curr = i
        return profit