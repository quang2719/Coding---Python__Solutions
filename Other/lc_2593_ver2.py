class Solution:
    def findScore(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return min(nums)

        s_num = [(x,i) for i,x in enumerate(nums)]
        s_num.sort(key = lambda x : x[0])
        res = 0
        checked = [False] * len(s_num)
        for val,id in s_num:  
            if not checked[id]:
                res += val
                if id == 0:
                    checked[id+1] = True
                elif id == len(nums)-1: checked[id-1] = True
                else: 
                    checked[id-1] = True 
                    checked[id+1] = True
        return res