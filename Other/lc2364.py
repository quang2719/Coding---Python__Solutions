class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        j - i = nums[j] - nums[i]
        j - nums[j] == i - nums[i]

        """
        n = len(nums)
        total_way = (n*(n-1))/2

        count = 0
        sub = {}
        for i in range(len(nums)):
            s = i - nums[i]
            sub[s] = sub.get(s,0)+1
        for v in sub.values():
            if v >=2:
                count += v*(v-1)/2
        return total_way - count
            