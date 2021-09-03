class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        lines = [[] for i in range(numRows)]
        state = 1
        index = 0
        if numRows == 1 :
            return s
        for char in s :
            if state == 1 and index<(numRows-1):
                lines[index].append(char)
                index = index + 1
            elif state==1 and index == (numRows-1) : 
                lines[index].append(char)
                state = 0
                index = index-1
            elif state==0 and index > 0 : 
                lines[index].append(char)
                index = index-1
            elif state==0 and index == 0 : 
                lines[index].append(char)
                state = 1
                index = index+1
                
        output = ""
        for i in lines :
            for char in i :
                output = output + char
        return output
                
                
            
            