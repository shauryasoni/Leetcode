class Solution:
    def ispalindrome(self,s,i,j,d) :
        if (i,j) in d :
            return d[(i,j)]
        
        if i == j :
            d[(i,j)] = 1
            return d[(i,j)]
        
        if len(s[i:j+1]) == 2:
            if s[i] == s[j] :
                d[(i,j)] = 1
                return d[(i,j)]
            else :
                d[(i,j)] = 0
                return d[(i,j)]
        
        elif s[i] != s[j] :
            d[(i,j)] = 0
            return d[(i,j)]

        else :
            d[(i,j)]  = self.ispalindrome(s,i+1,j-1,d)
            return d[(i,j)]
            
        
    def countSubstrings(self, s: str) -> int:
        d = {}
        n = 0
        for i in range(len(s)):
            for j in range(i,len(s)) :
                n = n +  self.ispalindrome(s,i,j,d)
        return n
