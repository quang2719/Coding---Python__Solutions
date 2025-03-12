# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        fre = {}
        ele = []
        iter_head = head
        while iter_head:
            fre[iter_head.val] = fre.get(iter_head.val,0)+1
            if fre[iter_head.val] == 1:
                ele.append(iter_head.val)
            iter_head = iter_head.next
        i = 0
        while i < len(ele):
            if fre[ele[i]] > 1:
                ele.pop(i)
            else: i+=1
        if not ele:
            return None
        while head and head.val != ele[0]:
            head = head.next
                
        iter_head = head
        i = 0
        while iter_head:
            if i == len(ele)-1: break
            cur_head = iter_head
            while iter_head.val != ele[i+1]:
                iter_head = iter_head.next
            i+=1
            cur_head.next = iter_head
        iter_head.next = None
        return head
                