from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if len(nums) == 1:
            pass
        else :
            
            index = 0
            while index <len(nums)-1 :
                if nums[index] >= nums[index+1] :
                    index +=1
                    continue
                else :
                    break
                
            if index == len(nums)-1 :   #checking if the string is descending
                i = 0
                j = l-1
                while i < j : #if yes, return reversed string
                    if i == j :
                        i+=1
                        j-=1
                        pass
                    else :
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        i+=1
                        j-=1
                    
            else :

                check = 0
                index = l-1
                s1 = 0
                s2 = 0
                while check == 0 and index>0: #Find first decreasing occurence, from the back. Swap with next minumum, reverse.
                    if nums[index] <=nums[index-1] :
                        index-=1
                    else :
                        s1 = index - 1
                        while index < l and nums[index]> nums[s1]:
                            index+=1
                        s2 = index - 1
                        temp = nums[s1]   #swap
                        nums[s1] = nums[s2]
                        nums[s2] = temp
                        i = s1+1
                        j = l-1
                        while i < j : #reverse
                            if i == j :
                                i+=1
                                j-=1
                                pass
                            else :
                                temp = nums[i]
                                nums[i] = nums[j]
                                nums[j] = temp
                                i+=1
                                j-=1
                        check+=1
#Print the next lexographic list permutation. (Dictionary order)
nums = [8,7,6,5,4,3,2,1]
(Solution().nextPermutation(nums))
print(nums)