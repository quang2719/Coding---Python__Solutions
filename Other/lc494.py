import numpy as np
class Solution:
    def __init__(self):
        self.res = 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = np.array(nums)
        m = np.array([1 for _ in range(len(nums))])
        self.createExpre(n,m,0,target,res)
        return res
    def createExpre(self,n,m,i,target,res):
        if i == len(n):
            if sum(n*m)==target:
                self.res+=1
        else:
            m[i] = 1
            self.createExpre(n,m,i+1,target,res)
            m[i] = -1
            self.createExpre(n,m,i+1,target,res)



        