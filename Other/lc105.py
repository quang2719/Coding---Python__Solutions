# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        queue = []
        available_id = 0
        range = {}
        inorder_map = {}
        for i,val in enumerate(inorder):
            inorder_map[val] = i

        iter_root = TreeNode(preorder[0])
        queue.append(iter_root)
        available_id +=1
        range[iter_root.val] = (0,len(preorder)-1)

        while queue:
            # queue to store node in next lever
            new_queue = []
            while queue:
                node = queue.pop(0)
                value = node.val
                left_bound,right_bound = range[value]
                node_inoder_id = inorder_map[value]

                if left_bound < node_inoder_id:
                    # add left leaf
                    node.left = TreeNode(preorder[available_id])
                    range[node.left.val] = (left_bound,node_inoder_id-1)
                    new_queue.append(node.left)
                    available_id+=1
                    if available_id == len(preorder):
                        return iter_root
                    
                if right_bound > node_inoder_id:
                    # add right leaf
                    node.right = TreeNode(preorder[available_id])
                    range[node.right.val] = (node_inoder_id+1,right_bound)
                    new_queue.append(node.right)
                    available_id+=1
                    if available_id == len(preorder):
                        return iter_root
            queue = new_queue
        return iter_root






