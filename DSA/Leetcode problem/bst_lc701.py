# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            node = TreeNode(val = val)
            root = node
        else:
            cur_node = root
            while True:
                if cur_node.val < val:
                    if cur_node.right is not None:
                        cur_node = cur_node.right
                    else:
                        node = TreeNode(val = val)
                        cur_node.right = node
                        break
                else:
                    if cur_node.left is not None:
                        cur_node = cur_node.left
                    else:
                        node = TreeNode(val = val)
                        cur_node.left = node
                        break
        return root 
            
