from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mincoins = [amount+1] * (amount+1)
        #print(mincoins)
        mincoins[0] = 0
        for i in range(1,amount+1) :
            for c in coins :
                if amount-c >=0:
                    mincoins[i] = min(mincoins[i],1+mincoins[i-c])
            #print(i,mincoins[amount])
        if mincoins[amount] >= amount+1 :
            return -1
        else:
            return mincoins[amount]
            
            
#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.
