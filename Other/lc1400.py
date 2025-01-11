from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= len([x for x,fre in Counter(s).items() if fre %2==1])
