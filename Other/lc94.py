# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inoder(root):
            if not root:
                return []
            res = []
            if root.left:
                res = res + inoder(root.left) 
            if root:
                res = res + [root.val] 
            if root.right:
                res = res + inoder(root.right) 
            return res
        return inoder(root)