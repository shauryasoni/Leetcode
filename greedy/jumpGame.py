#Greedy solution

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        if target == 0 :
            return True
        for i in range(target-1,-1,-1) :
            if i + nums[i] >= target :
                target = i
            #print(target)
            
        if target == 0 :
            return True
        else :
            return False

print(Solution().canJump([2,3,1,1,4]))