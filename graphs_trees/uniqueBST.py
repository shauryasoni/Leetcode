class Solution:
    def rec(self,start,end,d) :
        if (start,end) in d :
            return d[(start,end)]
        if start == end :
            d[(start,end)] = 1
            return d[(start,end)]
        
        if start > end :
            d[(start,end)] = 1
            return d[(start,end)]
        
        else :
            trees = 0
            for i in range(start,end+1) :
                trees = trees + self.rec(start,i-1,d)*self.rec(i+1,end,d) 
            #print(start,end,trees)
            d[(start,end)] = trees
            return d[(start,end)]
            
            
            
            
    def numTrees(self, n: int) -> int:
        d = {}
        res = self.rec(1,n,d)
        return res
        
            
            