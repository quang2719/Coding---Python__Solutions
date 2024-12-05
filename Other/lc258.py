class Solution:
    def addDigits(self, num: int) -> int:
        def add_digit(num):
            if num < 10: return num
            s = 0
            while num >0:
                s += num %10
                num//=10
            return add_digit(s)
        return add_digit(num)