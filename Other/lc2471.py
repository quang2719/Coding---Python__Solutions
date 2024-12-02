# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # bitree travel
        def dfs(head,level,arr_per_level):
            if not head:
                return
            if level not in arr_per_level.keys():
                arr_per_level[level] = [head.val]
            else:
                arr_per_level[level].append(head.val)
            dfs(head.left,level+1,arr_per_level)
            dfs(head.right,level+1,arr_per_level)
        # finding minimum swap to sort an array
        def minswap(arr):
            # create sorted array
            s_arr = sorted(arr)
            # create dict to find true index given a value
            v_to_i = {v:i for i,v in enumerate(s_arr)}
            # result
            res = 0
            visited = [False] * len(arr) 

            for i in range(len(arr)):
                # if element i are visited or it's true index: continue
                if visited[i] or arr[i] == s_arr[i]: continue

                # else: find the circle
                len_circle  = 1
                iter_i = v_to_i[arr[i]]
                visited[i] = True
                while arr[iter_i] != arr[i]:
                    visited[iter_i] = True
                    len_circle+=1
                    iter_i = v_to_i[arr[iter_i]]
                # number of swap will be len circle -1
                res += len_circle-1
            return res
        
        arr_per_level = {}
        dfs(root,0,arr_per_level)
        res = 0
        for level,arr in arr_per_level.items():
            res += minswap(arr)
        return res


        