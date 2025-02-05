# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        def dfs(root):
            if not root: return 0
            left_d, right_d = 0,0
            if root.left:
                left_d = dfs(root.left)
            if root.right:
                right_d = dfs(root.right)
            self.diameter = max(self.diameter,left_d+right_d+1)
            return max(left_d,right_d)+1
        dfs(root)
        return self.diameter