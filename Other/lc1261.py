# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.ele = set()
        self.root = root
        self.root.val = 0
        self.reconstruct(self.root)
    def reconstruct(self,node : Optional[TreeNode]):
        
        if not node: return
        self.ele.add(node.val)
        if node.left:
            node.left.val  = 2*node.val +1
            self.reconstruct(node.left)
        if node.right:
            node.right.val = 2*node.val + 2
            self.reconstruct(node.right)
        
        

    def find(self, target: int) -> bool:
        return target in self.ele
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)