from typing import List
class Solution:
    def findNeighbours(self,grid,i,j,visited,rows,columns) :
        if grid[i][j] == 0 :
            return
        if (i,j) in visited :
            return
        else :
            visited.add((i,j))
       
        if i > 0 :
            if grid[i-1][j] == "1" :
                self.findNeighbours(grid,i-1,j,visited,rows,columns)
        if i < rows-1 :
            if grid[i+1][j] == "1" :
                self.findNeighbours(grid,i+1,j,visited,rows,columns)
                   
        if j > 0 :
            if grid[i][j-1] == "1" :
                self.findNeighbours(grid,i,j-1,visited,rows,columns)
        if j < columns-1 :
            if grid[i][j+1] == "1" :
                self.findNeighbours(grid,i,j+1,visited,rows,columns)
               
               
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows = len(grid)
        columns = len(grid[0])
        stack = []
        for i in range(rows) :
            for j in range(columns) :
                if (grid[i][j] == "1") and ((i,j) not in visited) :
                    islands+=1
                   
                    self.findNeighbours(grid,i,j,visited,rows,columns)
                   
        return islands
print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
#Input: grid = [
#  ["1","1","0","0","0"],
 # ["1","1","0","0","0"],
 # ["0","0","1","0","0"],
 # ["0","0","0","1","1"]
#]
#Output: 3