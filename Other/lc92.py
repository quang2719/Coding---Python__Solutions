# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        if not head.next: 
            return head
        
        pad_node = ListNode(555)
        pad_node.next = head
        iter_head = pad_node
        
        while iter_head:
            if iter_head.next.val == left:
                left_node = iter_head
                iter_head = iter_head.next
                
                stack = []
                while iter_head.val != right:
                    stack.append(iter_head)
                    iter_head = iter_head.next
                
                right_node = iter_head.next
                left_node.next = iter_head
                left_node = left_node.next
                while stack:
                    new_node = stack.pop()
                    left_node.next = new_node
                    left_node = left_node.next
                left_node.next = right_node
            iter_head = iter_head.next
        return pad_node.next
                