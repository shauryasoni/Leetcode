a = "intention"
b = "execution"
res = ""
for i in range(1,len(a) + 1) :
    for j in range(1,len(b)+1) :
        if a[i-1] == b[j-1]:
            res+=a[i-1]
print (res)
