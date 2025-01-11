class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letter = set(s)
        res = 0
        for l in letter:
            mid = set()
            l = s.index(l)
            r = s.rindex(l)
            for i in range(l+1,r):
                mid.append(s[i])
            res += len(mid)
        return res
        