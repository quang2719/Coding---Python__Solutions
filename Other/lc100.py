# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.travelCheck(p,q)
    def travelCheck(self,p,q):
        if (not p) and (not q): #both none
            return True
        elif (not p) or (not q): 
            return False
        if p.val != q.val:
            return False
        else:
            return (
                True and 
                self.travelCheck(p.left,q.left) and 
                self.travelCheck(p.right,q.right)
            )