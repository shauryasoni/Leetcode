from typing import List
class Solution:
    def rec(self,index,amount,coins,d) :
        if (amount,index) in d :
            return d[(amount,index)]
        
        if amount == 0 :
            d[(amount,index)] = 1
            return d[(amount,index)]
        
        elif amount <0 :
            d[(amount,index)] =0
            return d[(amount,index)]
        
        if coins == [] and amount!=0 :
            
            d[(amount,index)] = 0
            return d[(amount,index)]
        if coins == [] and amount == 0 : 
            
            d[(amount,index)] = 1
            return d[(amount,index)]
        else :
            d[(amount,index)] = 0
            for i in range(index,-1,-1) :
                d[(amount,index)] =  d[(amount,index)] + self.rec(i,amount-coins[i],coins,d) 
            return d[(amount,index)]
        
    def change(self, amount: int, coins: List[int]) -> int:
        d = {}
        return self.rec(len(coins)-1,amount,coins,d)