class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        checked = [False for _ in range(len(nums)+1)]
        for x in nums:
            checked[x] = True
        checked[0] = True
        res = []
        for x,y in enumerate(checked):
            if not checked[x]:
                res.append(x)
        return res