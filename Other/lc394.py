class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i,x in enumerate(s):
            if x =='[':
                stack.append(i)
            elif x ==']':
                left = stack.pop()
                right = i
                n = left - 1
                while n >=0 and s[n].isdigit():
                    n-=1
                dup = int(s[n+1:left])
                print(f'handle left-{left} right-{right} dup -{dup}')
                if not stack:
                    print('push')
s = "2[abc]3[cd]ef"
print('s: ',s)
solu = Solution()
solu.decodeString(s)
                
s = "3[a2[c]]2[cd]ef"
print('s: ',s)
solu = Solution()
solu.decodeString(s)            
            