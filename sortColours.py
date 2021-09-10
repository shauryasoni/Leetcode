from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        two = len(nums)-1
        while two>=0 and nums[two]==2:
            two = two-1
        index = 0
        while index <= two :
            if nums[index] == 2 :
                temp = nums[index]
                nums[index] = nums[two]
                nums[two] = temp
                while two>=0 and nums[two]==2 :
                    two = two-1
            index+=1
        one = two
        
        while one>=0 and nums[one] == 1 :
            one = one-1
        index = 0
        while index <= one :
            if nums[index] == 1 :
                temp = nums[index]
                nums[index] = nums[one]
                nums[one] = temp
                while one>=0 and nums[one]==1 :
                    one = one-1
            index+=1