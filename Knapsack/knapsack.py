class Solution:
    #iterative
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[0 for i in range(W+1)] for j in range(len(wt) + 1)]
        r = len(dp)
        c = len(dp[0])
        for i in range(1,r) :
            for j in range(1,c) :
                
                if wt[i-1] <= j :
                    dp[i][j] = max(dp[i-1][j-wt[i-1]] + val[i-1], dp[i-1][j])
                else :
                    dp[i][j] = dp[i-1][j]
                    
                
        
                    
                  
        return(dp[r-1][c-1])