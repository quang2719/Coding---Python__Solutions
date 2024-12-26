# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_arr = [0]*k
        iter_node = head
        while iter_node:
            iter_node = self.reverseNextKElement(iter_node,k)
        return head
    def reverseNextKElement(self,node,k):
        cur_node = node
        if not cur_node:
            return None
        temp_arr = [0]*k
        for i in range(k):
            if not cur_node:
                return None
            temp_arr[i] = cur_node.val
            cur_node = cur_node.next
        cur_node = node
        for i in range(k):
            cur_node.val = temp_arr[(k-i-1)]
            cur_node = cur_node.next
        return cur_node