class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0 for _ in range(len(arr))]
        i = len(arr)-1
        while i >=0:
            if i == len(arr)-1:
                res[i] = -1
            else:
                res[i] = max(res[i+1], arr[i+1])
            i-=1
        return res