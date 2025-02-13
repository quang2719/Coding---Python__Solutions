class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <2: return 0
        check = [False for _ in s]
        stack = []
        for i,x in enumerate(s):
            if not  stack:
                stack.append((x,i))
            else:
                if stack[-1][0] == '(' and x ==')':
                    check[stack[-1][1]] = True
                    check[i] = True
                    stack.pop()
                else:
                    stack.append((x,i))
        
        left = 0
        res = 0
        while left < len(s)-1:
            if check[left]:
                right = left +1
                while (right < len(s)) and check[right]: 
                    right+=1
                if res < (right - left):
                    res = right - left
                left = right
            left +=1
        return res
            
                
            
s = ")()())"
solut = Solution()
print(solut.longestValidParentheses(s)   )                     
                         
                        
                