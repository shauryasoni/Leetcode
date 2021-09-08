from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        if len(nums) == 1 :
            return nums[0]
        gs = nums[0]
        cm = nums[0]
        for i in range(1,len(nums)) :
            
            cm = max(nums[i], cm + nums[i])
            if cm > gs :
                gs = cm
        return gs

print(Solution().maxSubArray([2,3,1,-2,4,5,6,7,-88,99]))