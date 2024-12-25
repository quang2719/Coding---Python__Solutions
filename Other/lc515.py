# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        level = 1
        self.treeTravel(root,dic,level)
        res = [y for x,y in dic.items()]
        return res
    def treeTravel(self,cur_node,dic,level):
        if not cur_node:
            return
        if level not in dic.keys():
            dic[level] = cur_node.val 
        else:
            dic[level] = max(dic.get(level),cur_node.val)
        self.treeTravel(cur_node.left,dic,level+1)
        self.treeTravel(cur_node.right,dic,level+1)


        