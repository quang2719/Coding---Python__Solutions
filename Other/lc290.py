class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = [x for x in s.split( )]
        if len(arr) != len(pattern): return False
        map_kv = {}
        map_vk = {}
        
        for i,x in enumerate(pattern):
            if x in map_kv:
                if not map_kv[x] == arr[i]: return False
            else:
                map_kv[x] = arr[i]
            
            if arr[i] in map_vk:
                if not map_vk[arr[i]] == x: return False
            else: 
                map_vk[arr[i]] = x
        return True