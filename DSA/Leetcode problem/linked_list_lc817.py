# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cur_point = head
        count = 0
        while cur_point != None:
            if cur_point.val in nums:
                count+=1
                nums.remove(cur_point.val)
                cur_point = cur_point.next
                while cur_point != None:
                    if cur_point.val not in nums:
                        break
                    nums.remove(cur_point.val)
                    cur_point = cur_point.next
            else:
                cur_point = cur_point.next
        return count
