from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxg = nums[0]
        mx = nums[0]
        mn = nums[0]
        for i in nums[1:] :
            temp = mx
            mx = max(i,mx*i,mn*i)
            mn = min(i,temp*i,mn*i)
            maxg = max(maxg,mx)
            
        return maxg
