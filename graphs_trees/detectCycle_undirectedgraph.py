class Solution:
    def dfs(self,node,visited,adj,previous)  :
        if node in visited : 
            return 1
        
        visited.add(node)
        for i in adj[node] :
            if i == previous :    # Undirected graph should not take into consideration the parent node, while calculating cycles.
                continue
            c = self.dfs(i,visited,adj,node)
            if c == 1 :
                return 1
            
        return 0

    def isCycle(self, V, adj):
    	#Code here
    	#print(V)
    	#print(adj)
	    visited = set()
	    for i in range(len(adj)) :
	        if i not in visited :
	            c = self.dfs(i,visited,adj,None)
	            if c == 1 :
	                return 1
		            
	    return 0

