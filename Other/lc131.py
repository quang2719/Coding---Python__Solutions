class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def part(nums,res):
            if nums not in res:
                res.append(nums.copy())

            for i in range(len(nums)):
                if i < len(nums) -1:
                    if nums[i] == nums[i+1]:
                        temp_num = nums.copy()
                        temp_num[i] = nums[i]+ nums[i+1]
                        temp_num[:] = temp_num[:i+1] + temp_num[i+2:]
                        part(temp_num,res)
                if i < len(nums)-2:
                    if nums[i] == nums[i+2]:
                        # backtrack
                        temp_num = nums.copy()
                        temp_num[i] = nums[i]+ nums[i+1] + nums[i+2]
                        temp_num[:] = temp_num[:i+1] + temp_num[i+3:] 
                        part(temp_num,res)
        nums = [x for x in s]
        res = []
        part(nums,res)
        return res