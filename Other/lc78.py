class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_state = []
        used = [False]*len(nums)
        
        def backtrack(cur_state,res,nums,used,pre_id):
            res.append(cur_state.copy())
            if len(cur_state) == len(nums):
                return

            for i in range(pre_id+1,len(nums)):
                x = nums[i]
                if not used[i]:
                    used[i] = True
                    cur_state.append(x)
                    backtrack(cur_state,res,nums,used,i)
                    used[i] = False
                    cur_state.pop()
        backtrack(cur_state,res,nums,used,-1)
        return res


