from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        l = []
        p = 1
        for i in range(len(nums)) :
            p = p*nums[i]
            d1[i] = p
     #   print(d1)
        p = 1
        for i in range(len(nums)-1,-1,-1) :
            p = p*nums[i]
            d2[i] = p
      #  print(d2)
        for i in range(len(nums)) :
            if i == 0:
                l.append(d2[i+1])
            elif i == len(nums) - 1 :
                l.append(d1[i-1])
            else :
                l.append(d1[i-1]*d2[i+1])
        return l
            
            
            
            
print(Solution().productExceptSelf([1,2,3,4,5,6]))