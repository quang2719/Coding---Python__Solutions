class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for x in s:
            if x.isdigit():
                if stack: stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)