class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.append(100)
        used = {}
        for x in nums:
            used[x] = False
        res  = []
        i = 0
        cur = []
        self.do(nums,res,i,cur,used)
        return res
    def do(self,nums,res,i,cur,used):
        if i == len(nums):
            res.append(cur.copy())
            return
        
        for x in nums:
            if x != 100:
                if not used[x]:
                    used[x] = True
                    cur.append(x)
                    self.do(nums,res,i+1,cur,used)
                    cur.pop()
                    used[x] = False
            else:
                self.do(nums,res,i+1,cur)
