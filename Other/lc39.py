class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_arr = []
        self.createArr(cur_arr,target,res,candidates,0)
        return res
    def createArr(self,cur_arr,target,res,candidates,i_candi):
        if target < 0: return
        if target == 0:
            res.append(cur_arr.copy())
            return
        
        for i in range(i_candi,len(candidates)):
            can = candidates[i]
            cur_arr.append(can)
            self.createArr(
                cur_arr,
                target - can,
                res,
                candidates,
                i
            )
            cur_arr.pop()

        