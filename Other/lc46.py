class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_arr = [0 for _ in nums]
        used = [False for _ in nums]
        self.P(0,cur_arr,used,nums,res)
        return res
    def P(self,i,cur_arr,used,nums,res):
        if i == len(nums):
            res.append(cur_arr.copy())
            return
        
        for id,x in enumerate(nums):
            if not used[id]:
                used[id] = True
                cur_arr[i] = x
                self.P(i+1,cur_arr,used,nums,res)
                used[id] = False

        