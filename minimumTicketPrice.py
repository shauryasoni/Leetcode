from typing import List
class Solution:
    def rec(self,days,costs,c,i,d) :
        if (c,i) in d :
            return d[(c,i)]
        if i == len(days) :
            d[(c,i)] = c
            return d[(c,i)]
        
        else :
            one = days[i] 
            index = i
            while days[index]<=one :
                index+=1
                if index == len(days) :
                    break
                
            c1 = self.rec(days,costs,c + costs[0],index,d)
            
            seven = days[i] + 6
            index = i
            while days[index]<=seven :
                index+=1
                if index == len(days) :
                    break
                
            c2 = self.rec(days,costs,c + costs[1],index,d)
            
            thirty = days[i] + 29
            index = i
            while days[index]<=thirty :
                index+=1
                if index == len(days) :
                    break
                
            c3 = self.rec(days,costs,c + costs[2],index,d)
            #print(i,days[i],c1,c2,c3)
            d[(c,i)] = min(c1,c2,c3)  
            return d[(c,i)]
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
       # dp = [max(costs)*len(days)]*days[-1]
        d = {}
        return self.rec(days,costs,0,0,d)
            
print(Solution().mincostTickets([1,4,6],[2,7,15]))