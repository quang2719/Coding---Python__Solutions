# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def BFS(root, target):
            if not root: return False
            queue = []
            queue.append([root,targetSum])
            while queue:
                head,target = queue.pop(0)
                if not head: continue
                target = target - head.val
                if target == 0 and not head.left and not head.right: return True
                
                queue.append([head.left,target])
                queue.append([head.right,target])
            return False
        return BFS(root,targetSum)


        