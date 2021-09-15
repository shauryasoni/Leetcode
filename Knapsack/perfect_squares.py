class Solution:
    """
    Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not
   """        
    def numSquares(self, n: int) -> int:
        if n == 1 :
            return 1

        i = 1
        num = 2
        squares = []
        while i <= n :
            squares.append(i)
            i = num*num
            num+=1
        
        if squares[-1] == n :
            return 1
        d = [10000 for i in range(n+1)]
        d[1] = 1
        d[0] = 0
        for number in range(n+1) :
            for i in squares :
                if number - i >=0 :
                    d[number]= min(d[number],1+d[number-i])
        return d[n]
            
            