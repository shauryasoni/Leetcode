from typing import List
#BFS approach. Increment number of jumps at every level. If the next level contains target index, return number of jumps.
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 0
        target = len(nums)-1
        visited = set()
        level = []
        frontier = [0]
        jumps = 0
        visited.add(0)
        while frontier!=[]:
            for i in frontier:
                j = nums[i]
                index = 1
                while i+index<=target and index<=j:
                    if i+index not in visited :
                        level.append(i+index)
                        visited.add(i+index)
                    if i + index == target :
                        return jumps + 1
                    index = index + 1
            frontier = level
            print(level)
            level = []
            jumps = jumps + 1
        return jumps 
                    
                    
            
            
        
        