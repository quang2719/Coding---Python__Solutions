"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    self.dicLevel = []
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
    def travel(self,node,level):
        if level == len(self.dicLevel):
            self.dicLevel.append([node.val])
        else:
            
        if node.left:
            self.travel(node.left. level+1)
        if node.right:
            self.travel(node.right,level+1)