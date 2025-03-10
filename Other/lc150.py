from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(f'stack: {stack}')
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                num = int(token)
                stack.append(num)
        return stack.pop()