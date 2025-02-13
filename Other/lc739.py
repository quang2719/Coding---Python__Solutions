class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        res = [0 for _ in range(len(temperatures))]
        
        for i,x in enumerate(temperatures):
            if not stack:
                stack.append((x,i))
            else:
                while stack:
                    cur,id = stack.pop()
                    if x > cur:
                        res[id] = i-id
                        # print('x,cur ,id',x,cur,id)
                    else:
                        stack.append((cur,id))
                        break
                stack.append((x,i))
            
        res[len(temperatures)-1] = 0
        return res
nums = [73,74,75,71,69,72,76,73]
solu = Solution()
print(solu.dailyTemperatures(nums))