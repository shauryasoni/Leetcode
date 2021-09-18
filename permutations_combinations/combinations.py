from typing import List
class Solution:
    def rec(self,i,n,k,res,curr) :
        if len(curr) == k :
            res.append(curr)
            return
        else :
            
            for i in range(i,n+1) :
                
                self.rec(i+1,n,k,res,curr + [i])
                
                continue
                
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.rec(1,n,k,res,[])
        return res

print(Solution().combine(7,3))
