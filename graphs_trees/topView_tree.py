class Solution:
    
    def tv(self,node,h,level,d) :
        if node == None :
            return
        if h in d :
            if d[h][1] > level :
                d[h] = [node.data,level]
        else :
            d[h] = [node.data,level]
        
        self.tv(node.left,h-1,level+1,d)
        self.tv(node.right,h+1,level+1,d)
        return
        
    def topView(self,root):
        d = {}
        res = []
        self.tv(root,0,0,d)
        #print(d)
        for i in sorted(d) :
            res.append(d[i][0])
        return res