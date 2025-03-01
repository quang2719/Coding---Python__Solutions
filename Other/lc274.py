class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        left = 0
        while left < len(citations) and (left+1) <= citations[left]:
            left+=1
        return left