class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        s_arr = sorted(arr)
        i = len(arr)-1
        res = []
        while i >= 0:
            cur = s_arr[i]
            j = arr.index(cur)
            if i ==j: 
                i-=1
                continue
            else:
                res.append(j+1)
                # pancake flip
                arr[:j+1] = arr[j::-1]
                #pancake flip 2
                res.append(i+1)
                arr[:i+1] = arr[i::-1]
                i-=1
        return res
        