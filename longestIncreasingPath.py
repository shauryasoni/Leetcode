"""
Given a matrix of N rows and M columns. From m[i][j], we can move to m[i+1][j], if m[i+1][j] > m[i][j], or can move to m[i][j+1] if m[i][j+1] > m[i][j]. The task is print longest path length if we start from (0, 0).

Recursive solution :

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def rec(self,A,i,j,last,count,d):
        if (i,j) in d :
            return d[(i,j)]
        if i>len(A)-1 or j>len(A[0])-1 :
            d[(i,j)] = 0
            return d[(i,j)]
        if i == len(A)-1 and j == len(A[0])-1 :
            if A[i][j] > last :
                d[(i,j)] =  count
                return d[(i,j)]
        if A[i][j] > last :
            p1 = self.rec(A,i+1,j,A[i][j],count + 1,d)
            p2 = self.rec(A,i,j+1,A[i][j],count + 1,d)
            d[(i,j)] = max(p1,p2)
            return d[(i,j)]
        else :
            d[i,j] =  0
            return d[(i,j)]
        

    def solve(self, A):
        d = {}
        mlength = self.rec(A,0,0,-1,1,d)
        if mlength == 0 :
            return -1
        else :
            return mlength
            
Iterative solution :
"""
class Solution :
    def solve(self, A) :
        dp = [[-1 for i in range(len(A[0]))] for i in range(len(A))]
        dp[0][0] = 1
        for i in range(1,len(A[0])) :
            if A[0][i] > A[0][i-1] :
                if dp[0][i-1]!= -1 :
                    dp[0][i] = dp[0][i-1] + 1
            

        for i in range(1,len(A)) :
                if A[i][0] > A[i-1][0] :
                    if dp[i-1][0]!= -1 :
                        dp[i][0] = dp[i-1][0] + 1
        
        for i in range(1,len(A)) :
            for j in range(1,len(A[0])) :
                e1 = -1
                e2 = -1
                if A[i][j] > A[i-1][j] :
                    if dp[i-1][j]!= -1 :
                        e1 = dp[i-1][j] + 1
                if A[i][j] > A[i][j-1] :
                    if dp[i][j-1]!=-1 :
                        e2 = dp[i][j-1] + 1
                dp[i][j] = max(e1,e2)
        return dp[len(A)-1][len(A[0])-1]
        for i in dp :
            print(i)



print(Solution().solve([
  [92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68],
  [100, 36, 95, 4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45, 63, 58],
  [38, 60, 24, 42, 30, 79, 17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47],
  [6, 91, 30, 71, 51, 7, 2, 94, 49, 30, 24, 85, 55, 57, 41, 67, 77],
  [32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42, 34, 16, 40, 59, 5],
  [31, 78, 7, 74, 87, 22, 46, 25, 73, 71, 30, 78, 74, 98, 13, 87, 91],
  [62, 37, 56, 68, 56, 75, 32, 53, 51, 51, 42, 25, 67, 31, 8, 92, 8],
[38, 58, 88, 54, 84, 46, 10, 10, 59, 22, 89, 23, 47, 7, 31, 14, 69]
]
))