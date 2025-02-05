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
        def travel(node,statep,stateq,p,q,state,res):
            if not state or not node:
                return
            
            if node.val == p:
                statep = True
            if node.val == q:
                stateq = True
            if node.left:
                travel(node.left,statep,stateq,p,q,state,res)
            if node.right:
                travel(node.right,statep,stateq,p,q,state,res)

            # res
            if stateq and statep:
                state = False
                res = node.val
                return
        res = 0
        travel(root,False,False,p,q,True,res)
        return res
            