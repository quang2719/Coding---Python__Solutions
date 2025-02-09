class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            code = self.createCode(s)
            if code not in dic.keys():
                dic[code] = [s]
            else:
                dic[code].append(s)
        res = [x for x in dic.values()]
        return res 
    def createCode(self,s):
        ch = [x for x in s]
        ch.sort()
        i = 0
        res = []
        while i < len(s):
            j = i
            while j < len(s) and ch[i] == ch[j]:
                j+=1
            res.append(ch[i])
            res.append(f'{j-i}')
            i = j
        return ''.join(res)