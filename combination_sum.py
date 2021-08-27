from typing import List
class Solution:

    def __init__(self) : 
        self.res = []
        self.nd = set()
        
        
        
    def rec (self,l,t,s,tl) :
        if s == t : 
            self.nd.add(tuple(sorted(tl)))
            return
        if s > t : 
            
            return None
        elif s<t : 
            for i in l : 
                tl.append(i)
                self.rec(l,t,s+i,tl)
                tl.pop(-1)  
             
        
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = sorted(candidates)
        l = l[::-1]
        index = 0
        while( index<len(l)and l[index]> target) :
            index = index + 1
        
        l = sorted(l)
        for i in l   :
            val = self.rec(l,target,i,[i])
    
        return  list(self.nd) 
        