class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_arr = []
        self.createArr(cur_arr,target,res,candidates)
        return res
    def createArr(self,cur_arr,target,res,candidates):
        if target < 0: return
        if target == 0:
            res.append(cur_arr)
            return
        
        for can in candidates:
            cur_arr.append(can)
            self.createArr(
                cur_arr,
                target - can,
                res,
                candidates
            )
            cur_arr = cur_arr[::-1]


        