from typing import List
class Solution:
    
    def rec(self,nums,target,s,l,d) :
        if (nums,s) in d :
            return d[(nums,s)]
        if nums == () and s == target :
            return 1
        elif nums == () :
            return 0
        else :
            d[(nums,s)] = self.rec(nums[:l],target,s+nums[l],l-1,d)+self.rec(nums[:l],target,s-nums[l],l-1,d)
            return d[(nums,s)]
            
    def findTargetSumWays(self, nums: List[int], target: int) -> int :
        d = {}
        return self.rec(tuple(nums),target,0,len(nums)-1,d)
        
#Target sum is a template problem

