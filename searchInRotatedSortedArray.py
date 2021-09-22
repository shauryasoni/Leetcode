from typing import List
#If we find middle index, one subarray is definitely sorted. Call binary search on the sorted half. else, repeat.

class Solution:
    def binarySearch(self,nums,start,end,target) :
        
        while start <= end : 
            middle = start + (end-start)//2
            if nums[middle] == target :
                return middle
            elif target > nums[middle]  : 
                start = middle + 1
            else :
                end = middle - 1
        return -1


        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 :
            if nums[0] == target :
                return 0
            else :
                return -1
            
        start = 0
        end = len(nums) - 1
        
        while start <= end :
            
            middle = start + ( end - start )//2
            
            if nums[middle] == target :
                return middle
            
            if nums[start]  <= nums[middle] :
                found = self.binarySearch(nums,start,middle,target)
                if found!= -1 :
                    return found
                else :
                    start = middle + 1
                    
                
            else :
                found = self.binarySearch(nums,middle,end,target)
                if found != -1 :
                    return found
                else :
                    end = middle - 1
        return -1
            