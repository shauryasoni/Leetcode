"""
#Variation of target sum. 

Recursive Solution, Accepted but very slow

class Solution:
    def rec(self,nums,i,s1,s2,d) :
        if (i,s1,s2) in d :
            return d[(i,s1,s2)]
        if s1 == s2 and i <0:
            d[(i,s1,s2)] = True
            return d[(i,s1,s2)]
            
        if i < 0 :
            d[(i,s1,s2)] = False
            return d[(i,s1,s2)]
        else :
            d[(i,s1,s2)] = self.rec(nums,i-1,s1+nums[i],s2,d) or self.rec(nums,i-1,s1,s2 + nums[i],d)
            return d[(i,s1,s2)]
        
    def canPartition(self, nums: List[int]) -> bool:
        d = {}
        return self.rec(nums,len(nums)-1,0,0,d)
"""




