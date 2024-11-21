# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        loop  = True
        def balance_tree(node,level):
            global loop
            if not loop:
                return False
            
            l,r = level
            if node.left is not None:
                l += find_depth(node.left)
            if node.right is not None:
                r+= find_depth(node.right)
            
                        
        