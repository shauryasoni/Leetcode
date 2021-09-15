class Solution:
	# @param A : tuple of integers
	# @return an integer
    #Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    #Given [100, 4, 200, 1, 3, 2],

    #The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
    def longestConsecutive(self, A):
        ele = set()
        m = 1
        for i in A :
            ele.add(i)

        visited = set()
        for i in A :
            c = 0
            if i in visited :
                continue
            else  :
                start = i - 1
                end = i + 1
                c = 1
                while end in ele :
                    visited.add(end)
                    c+=1
                    end = end + 1
                while start in ele :
                    visited.add(start)
                    c+=1
                    start = start - 1
            if c > m :
                m = c
        return m