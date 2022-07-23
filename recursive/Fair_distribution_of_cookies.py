class Solution:
    
    def rec(self, i, cookies, dist, top) :
        
        if i == len(cookies) :
            return top
            
        
        else :
            munf = 1000000
            for j in range(len(dist)):
                    
                dist[j] += cookies[i]
                prev = top
                if dist[j] > top :
                    top = dist[j]
                munf = min(munf, self.rec(i+1, cookies, dist, top))
                
                top = prev
                dist[j] = dist[j] - cookies[i]
                    
            return munf
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k  == len(cookies) :
            return max(cookies)
        
        top = -1
        dist = [ 0 for i in range(k)]
        
        return self.rec(0,cookies, dist,top)
