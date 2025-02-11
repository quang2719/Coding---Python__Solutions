class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack = []
        for x in s:
            stack.append(x)
            if len(stack) < len(part):
                continue 
                       
            r = len(stack)-1
            check = True
            for i in range(len(part)-1,-1,-1):
                if part[i]!= stack[r + i-len(part)+1]:
                    check = False
                    break
            if check:
                remove = len(part)
                while remove > 0:
                    stack.pop()
                    remove-=1
        return ''.join(stack)
                
s = "axxxxyyyyb"
part = 'xy'
solu = Solution()
print(solu.removeOccurrences(s,part))

        