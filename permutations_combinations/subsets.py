from typing import List
class Solution:
    def rec(self,nums,res,curr) :
        if nums == [] :
            res.append(curr)
            return
            
        else :
            self.rec(nums[:-1],res,curr+[nums[-1]])
            self.rec(nums[:-1],res,curr)
            return
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.rec(nums,res,[])
        return res
    
print(Solution().subsets([1,2,3,4,5,6,7,8,9]))