class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count_n_digit(n, k):
            if n==1: return k   
            res = 0
            for i in range(1,k+1):
                res += count_n_digit(n-1,i)
            return res
        return count_n_digit(n,5)