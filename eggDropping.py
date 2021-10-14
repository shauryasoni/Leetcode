import sys
#passes in geeks for geeks
class Solution:
    def rec(self,k,n,d) :
        
        if (k,n) in d :
            return d[(k,n)]
        
        if n == 0:
            return 0
        if n == 1 :
            return 1
        if k == 1 :
            d[(k,n)] = n
            return d[(k,n)]
        else :
            minmoves = sys.maxsize
            for i in range(1,n+1) :
                
                breaks = 1 + self.rec(k-1,i-1,d)
                nobreak = 1 + self.rec(k,n-i,d)
                
                minmoves = min(max(breaks,nobreak),minmoves)
            
            d[(k,n)] = minmoves
            return d[(k,n)]
                
         
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1 :
            return n
        if n == 0 or n == 1 :
            return n
        d = {}
        res = self.rec(k,n,d)
        return res