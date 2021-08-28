class Solution:        
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word2)+1
        c = len(word1)+1
        matrix = []
        for i in range(r) :
            row = [0]*c
            matrix.append(row)
        for i in range(len(matrix)) :
            matrix[i][0] = i
        for j in range(len(matrix[0])):
            matrix[0][j] = j
        print (matrix)
        for i in range(1,r) :
            for j in range(1,c) :
                if word1[j-1] == word2[i-1] :
                    matrix[i][j] = matrix[i-1][j-1]
                else :
                    matrix[i][j] = 1 + min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
        return matrix[r-1][c-1]
#Levinstein algorithm