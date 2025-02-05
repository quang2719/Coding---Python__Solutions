# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.count = 0
        self.target = targetSum
        def candidate_sum(root):
            if not root: return []
            cur_candi = [root.val]

            if root.right:
                right_candi = candidate_sum(root.right)
                for x in right_candi:
                    cur_candi.append(x+root.val)
            if root.left:
                left_candi = candidate_sum(root.left)
                for x in left_candi:
                    cur_candi.append(x+root.val)
            self.count += cur_candi.count(self.target)
            return cur_candi
        candi = candidate_sum(root)
        return self.count