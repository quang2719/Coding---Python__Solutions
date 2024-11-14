# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not head: return res

        next_node_dict = set()
        while head.next is not None:
            if head.next in next_node_dict:
                res = head.next
                break
            else: 
                next_node_dict.add(head)
                head = head.next
        return res
            