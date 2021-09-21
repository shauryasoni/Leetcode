from typing import List
#Dynamic programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        if len(nums) == 1 :
            return 1
        
        mx = 1
        j = 1
        for j in range(1,len(nums)):
            for i in range(0,j) :
                if nums[j] > nums[i] :
                    if dp[i] + 1 > dp[j] :
                        dp[j]+=1
                if dp[j]>mx :
                    mx = dp[j]
        return mx                        
                       
            
            
            
        