#Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = 1
        l = len(temperatures)
        if l == 1 :
            return [0]
        ans = [-1 for i in range(l)]
        ans[-1] = 0
        index = 0
        while n!=l :
            
            if index == l :
                index = 0
                
            if ans[index] != -1 :
                index+=1
                
            if ans[index] == -1 :
                i = index + 1
                while i < l and temperatures[i] <= temperatures[index] :
                    i+=1
                if i != l:
                    ans[index] = i - index
                    n+=1
                else :
                    ans[index] = 0
                    n+=1
        return ans   