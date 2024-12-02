def minswap(arr):
    s_arr = sorted(arr)
    v_to_i = {v:i for i,v in enumerate(s_arr)}
    res = 0
    visited = [False] * len(arr) 

    for i in range(len(arr)):
        if visited[i] or arr[i] == s_arr[i]: continue

        len_circle  = 1
        iter_i = v_to_i[arr[i]]
        visited[i] = True
        while arr[iter_i] != arr[i]:
            visited[iter_i] = True
            len_circle+=1
            iter_i = v_to_i[arr[iter_i]]
        res += len_circle-1
    return res
arr = [1,3,2]
print(minswap(arr))

    
