class Solution:
    def __init__(self) :
        self.ans = set()
    
    def rec(self,l,s,curr,target) : 
         
        
        if(s == target) : 
            self.ans.add(tuple((curr)))
            return
            
        if s> target :
            return None
        
        if (l==[]) : 
            return
        
        elif s < target : 
            for i in range(len(l)) :
                if (i and l[i]==l[i-1]) : 
                    continue
                self.rec(l[i+1:],s+l[i],curr+[l[i]],target)
                
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==1 and candidates[0]==target: 
            return [[candidates[0]]]
        
        l = sorted(candidates)
        self.rec(l,0,[], target)
        return list(self.ans)