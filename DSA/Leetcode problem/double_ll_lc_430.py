"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur_point = head
        while(cur_point is not None):
            if cur_point.child is not None:
                child_node = self.flatten(cur_point.child)
                next_node = cur_point.next

                cur_point.next = child_node
                child_node.prev = cur_point
                cur_point.child = None

                while child_node.next is not None:
                    child_node = child_node.next
                child_node.next = next_node
                if next_node is not None:
                    next_node.prev = child_node
                
                cur_point = next_node
            else:
                cur_point = cur_point.next
        return head
        