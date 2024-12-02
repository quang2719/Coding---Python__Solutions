class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!= sorted_list[i]:
                count+=1
        return count
        