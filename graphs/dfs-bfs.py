graph = {
    1:[2,3],2:[1,4],3:[1,5],4:[2],5:[3],6:[],7:[8],8:[7],9:[]
    }
def dfs(graph) :
    
    count  = 0
    visited = set()
    stack = []
    nodes= 0
    for i in graph :
        if i in visited :
            continue
        else :
            stack.append(i)
            while stack!=[] :
                node = stack.pop()
                nodes+=1
                visited.add(node)
                for i in graph[node] :
                    if i in visited :
                        continue
                    stack.append(i)
                #print(stack)
            if nodes>=2:
                count+=1
                nodes = 0
    print(count)
        
#dfs(graph)

def bfs(graph) :
    visited = set()
    level = []
    frontier = []
    expanded = 0
    frontier.append(1)
    for i in graph :
        if i not in visited :
            frontier.append(i)
            print(frontier,expanded)
        else :
            continue
        while frontier!=[] :

            for node in frontier :

                if node not in visited:
                    visited.add(node)
                    for v in graph[node] :
                        if v not in visited :
                            level.append(v)

            frontier = level
            expanded+=1
            print(frontier,expanded)
            level = []
bfs(graph)               

