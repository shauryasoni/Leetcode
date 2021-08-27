class Solution:
    def rec(self,s1,s2,i,j,d) :
        if (i,j) in d :
            return d[(i,j)]
        if i<len(s1) and j<len(s2):
            if s1[i] == s2[j] :
                d[(i,j)] = 1 + self.rec(s1,s2,i+1,j+1,d)
                return d[(i,j)]
            else :
                d[(i,j)] =  max(self.rec(s1,s2,i+1,j,d),self.rec(s1,s2,i,j+1,d))
                return d[(i,j)]
        else :
            d[i,j] =  0
            return d[(i,j)]
        
        
            
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 =="" or text2 == "":
            return 0
        
        else :
            d = {}
            i = 0
            j = 0
            return self.rec(text1,text2,i,j,d)
