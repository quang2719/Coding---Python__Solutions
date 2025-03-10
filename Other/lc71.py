class Solution:
    def simplifyPath(self, path: str) -> str:
        ele = []
        i = 0
        while i < len(path):
            if path[i] != '/':
                j = i
                while j < len(path) and path[j] != '/':
                    j+=1
                ele.append(path[i:j])
                i = j
            else: i+=1
        res = []
        for x in ele:
            if x == '.': continue
            if x == '..':
                if res: res.pop()
            else:
                res.append(x)
        if not res: return '/'
        return '/'.join(res)
    