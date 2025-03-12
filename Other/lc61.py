# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        ele = []
        while head:
            n+=1
            ele.append(head)
            head = head.next
        k = k%n
        if k == 0:
            return head
        while k:
            x = ele.pop()
            ele.inset(0,x)
        head = ele[0]
        for i in range(len(ele)):
            if i == len(ele)-1:
                ele[i].next = None
            ele[i].next = ele[i+1]
        return head
