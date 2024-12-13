# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur_head = dummy
        heap = []
        count = 0 # using when 2 element have same value

        # Push the head of each list into the heap
        for l in lists:
            count+=1
            if l:
                heapq.heappush(heap, (l.val,count, l))

        while heap:
            val, _, cur = heapq.heappop(heap)
            cur_head.next = ListNode(val)
            cur_head = cur_head.next

            if cur.next:
                count+=1
                heapq.heappush(heap, (cur.next.val,count, cur.next))
                

        return dummy.next