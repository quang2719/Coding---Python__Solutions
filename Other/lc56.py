class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        stack = []
        for start,end in intervals:
            if not stack:
                stack.append([start,end])
            else:
                pre_start,pre_end = stack.pop()
                if pre_end >= start:
                    new_end = max(pre_end,end)
                    new_start = min(pre_start,start)
                    stack.append([new_start,new_end]) 
                else: 
                    stack.append([pre_start,pre_end])
                    stack.append([start,end])
        return stack