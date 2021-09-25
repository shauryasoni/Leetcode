from typing import List
class Solution:

#DETECT CYCLE IN DIRECTED GRAPH. KET POINT : UNMARK A NODE AS VISITED EVERYTIME YOU BACKTRACK. 
    def cycle(self,node,visited,adj,d) :
        if node in d :
            return d[node]
        
        if node in visited : 
            d[node] =  True
            return d[node]
        else :
            visited.add(node)   #MARK VISITED
            for i in adj[node] :
                c = self.cycle(i,visited,adj,d)
                if c == True :
                    d[node] = True
                    return d[node]
            visited.remove(node)   #UNMARK VISITED
            d[node] = False
            return d[node]
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range((numCourses))]
        for i in prerequisites :
            adj[i[1]].append(i[0])
        #print(adj)
        visited = set()
        d = {}
        c = False
        for i in range(len(adj)) :
            
            c = self.cycle(i,visited,adj,d)
            if c == True :
                return False
            visited = set()
        return True
            