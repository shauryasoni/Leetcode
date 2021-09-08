from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        elif len(nums)== 1 and nums[0]==target:
            return [0,0]
        elif  len(nums)== 1 and nums[0]!=target:
            return [-1,-1]
        else :
            start = 0
            end = len(nums)-1
            middle = (end - start)//2
            
            while end >= start :
                #print(start,middle,end)
                if nums[middle] == target :
                    s = middle
                    e = middle
                    c = 0
                    while s>=0 and nums[s] == target :
                        s = s -1 
                    while e<=len(nums)-1 and nums[e] == target :
                        e = e + 1
                    return [s+1,e-1]
                
                if target > nums[middle] :
                    start = middle+1 
                    middle = start + (end - start) //2
                    
                else :
                    end = middle-1
                    middle = start + (end-start)//2
                    
            return [-1,-1]