# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        def travel(parent,root):
            if not root: return
            if root.left:
                parent[root.left] = root
                travel(parent,root.left)
            if root.right:
                parent[root.right] = root
                travel(parent,root.right)
        travel(parent,root)

        candidate = []
        while p != root:
            candidate.append(p)
            p = parent[p]
        candidate.append(p)
        
        while q != root:
            if q in candidate:
                return q
            q = parent[q]
        return root