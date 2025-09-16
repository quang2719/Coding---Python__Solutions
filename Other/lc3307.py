from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def recur (k, op,i):
            if i == 0:
                if op[i] == 0:
                    return 0
                else: 
                    return 0 if k == 1 else 1
                        
            n = i + 1
            l = 2**n
            if k > l/2:
                if op[i] == 0:
                    return recur(k-l/2, op,i-1)
                else:
                    return 1 + recur(k-l/2, op,i-1)
            else:
                return recur(k, op,i-1)
        return chr(ord('a')+ recur(k,operations,len(operations)-1)%26)

# k = 5
# operations = [0,0,0]
k = 10
operations = [0,1,0,1]
solu = Solution()
print(solu.kthCharacter(k,operations))