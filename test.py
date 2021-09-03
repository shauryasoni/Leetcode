ans = []
def rec(valid,res,missing,s,target,index) :
    global ans
    if len(res) > missing :
        return False
    if len(res) == missing :
        if s == target :
            ans.append(tuple(res))
            return True
    if s > target :
        return False
    else :
        for i in range(index,len(valid)) :
            res.append(valid[i])
            something = rec(valid,res,missing,s+valid[i],target,i)
            if something == True :
                return True
            res.pop(-1)
        return
    
    

def solution(A, F, M):
    global ans
    # write your code in Python 3.6
    length = len(A)
    s = sum(A)
    total = (M*1.0) * (length + F)
    d = {}
    rec([1,2,3,4,5,6],[],F,0,total-s,0)
    print(ans)
    
print(solution([1,5,6],4,3))