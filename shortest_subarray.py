from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
    
        res = len(nums) + 1
        for i in range(len(nums)) : 
            s=  nums[i]
            if s>=k : 
                return 1
            for j in range(i+1,len(nums)) : 
                
                s = s + nums[j]
                if s>=k : 
                    if j-i+1 <res :
                        res = j-i + 1
                    
                    break
        if res>len(nums) : 
            return -1
        else : 
            return res
print(Solution().shortestSubarray([56,-21,56,35,-9],61))