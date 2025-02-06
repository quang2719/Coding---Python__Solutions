class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 4: return 0
        self.cache = {0:1,1:1}
        def factorial(n):
            if n in self.cache.keys():
                return self.cache[n]
            else:
                res = n * factorial(n-1)
                self.cache[n] = res
                return res
        if len(nums) <= 3: return 0
        nums.sort()
        count = 0
        pow_two_num = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p = nums[i]*nums[j]
                pow_two_num[p] = pow_two_num.get(p,0) +1
        count = 0
        for fre in pow_two_num.values():
            if fre >=2:
                count += factorial(fre)/(factorial(2)*factorial(fre-2))
        return int(count*8)
nums = [2,3,4,6]
solution = Solution()
print(solution.tupleSameProduct(nums))