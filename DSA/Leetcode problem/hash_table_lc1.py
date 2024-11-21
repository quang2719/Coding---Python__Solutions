class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            if dic.get(target - num, -1) != -1:
                return [i,dic[target - num]]
            else:
                dic[num] = i
                    
        