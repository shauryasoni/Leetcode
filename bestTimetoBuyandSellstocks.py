from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 :
            return 0
        maxprofit = 0
        minyet = prices [0]
        for i in prices[1:] :
            if i < minyet :
                minyet = i
            else :
                if i > minyet :
                    if i-minyet > maxprofit :
                        maxprofit = i-minyet
        return maxprofit