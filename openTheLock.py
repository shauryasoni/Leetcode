from typing import List
#BFS solution


    
class Solution:
    
    def getCombo(self,src) :
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res
            
        
        
    def openLock(self, deadends: List[str], target: str) -> int:
        for i in deadends :
            if i == "0000" :
                return -1
        else :
            
            visited = set(deadends)
            frontier = ["0000"]
            level = []
            turns = 0
            while frontier :
                
                for i in frontier :
                    if i == target :
                        return turns
                    if i in visited :
                        continue
                    visited.add(i)
                    expansion = self.getCombo(i)
                    level.extend(expansion)
                    
                frontier = level
                #print(frontier)
                level = []
                turns+=1
            return -1

print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888"))