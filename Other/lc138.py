"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = set()
        val  = head.val
        random = Node(head.random,None,None)
        new_head = Node(val,None,random)
        while head.next:
            cur = head.next
            
        