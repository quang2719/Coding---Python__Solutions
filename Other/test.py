class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(x) for x in s.split()]
        ones = sum(nums)
        cnt_one = 0
        res = 0
        for i in range(len(nums)-1):
            if nums[i] == 1:
                cnt_one+=1
            res = max(res,(i+1-cnt_one)+(ones-cnt_one))
        return res