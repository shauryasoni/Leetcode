from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        
        
        r = len(matrix)
        c = len(matrix[0])
        g = 0
        
        for i in range(c) :
            if matrix[0][i] == "1" :
                dp[0][i] = 1
                g = 1
            else :
                dp[0][i] = 0
                
        for i in range(r) :
            if matrix[i][0] == "1" :
                dp[i][0] = 1
                g = 1
            else :
                dp[i][0] = 0
            
        for i in range(1,r) :
            for j in range(1,c) :
                if matrix[i][j] == "1" :
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    
                if dp[i][j] > g :
                    g = dp[i][j]
        return g*g
                
        