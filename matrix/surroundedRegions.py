from typing import List
class Solution:
    
    def os(self,board,visited,group,r,c,i,j) :
        if board[i][j] == "X" :
            return True
        if i == 0 or i == r-1 :
            return False
        if j == 0 or j == c-1 :
            return False
        
        if (i,j) in visited :
            return True
        elif board[i][j] == "O":
            visited.add((i,j))
            group.append((i,j))
            ri = self.os(board,visited,group,r,c,i,j+1)
            l = self.os(board,visited,group,r,c,i,j-1)
            u = self.os(board,visited,group,r,c,i-1,j)
            d = self.os(board,visited,group,r,c,i+1,j)
        
            return True and ri and l and u and d
        
        
    def solve(self, board: List[List[str]]) -> None:

        visited = set()
        captured = []
        r = len(board)
        c = len(board[0])
        for i in range(1,len(board)-1) :
            for j in range(1, len(board[0])-1) :
                if (i,j) in visited :
                    continue
                    
                elif board[i][j] == "O" :
                    group = []
                    corno = self.os(board,visited,group,r,c,i,j)
                    if corno == True :
                        captured.append(group)
       # print(captured)
        for i in captured :
            for j in i :
                board[j[0]][j[1]] = "X"
        
        
        