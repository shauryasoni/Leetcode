def merge(arr) :
    if len(arr) == 0 :
        return []
    if len(arr) == 1 :
        return arr

    else :
        mid = len(arr)//2
        left = merge(arr[:mid])
        right = merge(arr[mid :])
        # print(left, right)

        temp = []
        n = len(left)
        m = len(right)

        i,j = 0,0
        while i < n and j < m :
            
            if left[i] <= right[j] :
                temp.append(left[i])
                i+=1
            else :
                temp.append(right[j])
                j+=1
        if i == n :
            temp = temp + right[j:]
        elif j == m :
            temp = temp + left[i:]
        return temp
