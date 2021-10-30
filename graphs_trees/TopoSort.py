class Solution:
    def topo(self,adj,v,res,visited) :
        if visited[v] == 1 :
            return
        else :
            visited[v] = 1
            for i in adj[v] :
                self.topo(adj,i,res,visited)
            res.append(v)
            #(res)
            return
            
        
    def topoSort(self, v, adj):
        # Code here
        #print(adj,v)
        visited = [0 for i in range(v)]
        res = []
        for i in range(v) :
            if visited[i] == 0 :
                self.topo(adj,i,res,visited)
        #print(res)     
        return  res[::-1]
        