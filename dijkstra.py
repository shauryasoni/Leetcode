    def dijkstra(self, V, adj, S):
        #code here
        #print(V,adj,S)
        dis = [100000 for i in range(V)]
        visited = [ 0 for i in range(V)] 
        dis[S] = 0
        v = 0
        u = 0
        curr = S
      
        while v < V and curr!=None:
            u = 10000
            curr = None
            for i in range(V) :   #find shortest path from available distances
                if visited[i] == 0 :
                    if dis[i] < u :
                        u = dis[i]
                        curr = i
                        # print(curr,dis)
            if curr!=None :
            
                visited[curr] = 1
                v +=1
                for i in adj[curr] :
                    if visited[i[0]] == 0 :
                        if u + i[1] < dis[i[0]] :
                            dis[i[0]] = u + i[1]
            
                
        return dis
