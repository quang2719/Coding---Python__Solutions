class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_kv = {}
        map_vk = {}
        for i,x in enumerate(s):
            if x in map_kv:
                if map_kv[x] != t[i]: return False
            else:
                map_kv[s[i]] = t[i]
            if t[i] in map_vk:
                if map_vk[t[i]] != x: return False
            else:
                map_vk[t[i]] = x
    
        return True