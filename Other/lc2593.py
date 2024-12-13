from queue import PriorityQueue
class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        checked = set()
        pq = PriorityQueue()
        for i,x in enumerate(nums):  pq.put((x,i))

        while not pq.empty():
            val,id = pq.get()
            if id not in checked:
                res += val
                checked.add(id)
                if id == 0:
                    checked.add(id+1)
                elif id == len(nums)-1: checked.add(len(nums)-2)
                else: 
                    checked.add(id-1)
                    checked.add(id+1)
        return res