from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1 :
            return 1
        
        n = 1
        i = 1
        m = 1
        last = 0
        state = None  #      1 => greater than   , 0 => lesser than
        
        while i<len(arr) :
            if n == 1 :
                if arr[i] > arr[last] :
                    print(i)
                    n+=1
                    state = 1
                    last = i
                    i+=1
                    
                elif arr[i] < arr[last] :
                    print(i)
                    n+=1
                    state = 0
                    last = i
                    i+=1
                else :
                    print("done")
                    print(i)
                    last = i
                    i+=1
                    n = 1
            else :
                if arr[i] > arr[last] and state == 0 :
                    print(i)
                    n+=1
                    state = 1
                    last = i
                    i+=1
                elif arr[i] < arr[last] and state == 1 :
                    print(i)
                    n+=1
                    state = 0
                    last = i
                    i+=1
                elif arr[i] == arr[last] :
                    print("done")
                    print(i)
                    n = 1
                    last = i
                    i+=1
                else :
                    last = i
                    i+=1
                    n = 2
        
            if n > m :
                m = n
        if n > m :
            m = n
        return m
    
                    