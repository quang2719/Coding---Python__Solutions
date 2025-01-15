class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        count_open = 0
        count_close = 0

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(': count_open +=1
                else: count_close += 1

                if count_close > count_open:
                    if stack:
                        stack.pop()
                        count_close -=1
                    else: return False
            else:
                stack.append(s[i])
        return stack
        if len(stack) %2 == 0: return True
        return False



solution = Solution()
s =    "()()((()))(("
lock = "111111101101"
print(solution.canBeValid(s,lock))