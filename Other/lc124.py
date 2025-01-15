# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxBranch(root,cache):
            cleft_val,right_val = 0,0
            if not root.left:
                left_val = -float('inf')
            else:
                left_val = maxBranch(root.left,cache)
            if not root.right:
                right_val = -float('inf')
            else:
                right_val = maxBranch(root.right,cache)
            cur_val = root.val

            max_sum = max(
                cur_val,
                # can not recusion left and right if not choose 
                # cur val (path will not connected)
                # left_val,
                # right_val,
                cur_val+left_val,
                cur_val+right_val,
                # same with both left and rightright
                # cur_val+left_val+right_val
            )
            cache.append(max(
                max_sum,
                # but left and right can me maximum itself.
                left_val,
                right_val,
                cur_val+left_val+right_val
            ))
            return max_sum
        cache = []
        maxBranch(root,cache)
        return max(cache)