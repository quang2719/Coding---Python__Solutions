import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for x in nums:
            table[x] = table.get(x,0) + 1
        fre = []
        iter = 0
        for key,val in table.items():
            if iter < k:
                # push to min heap
                heapq.heappush(
                    fre,
                    (val,key)
                )
            else:
                cur_top = fre[0][0]
                if val > cur_top:
                    heapq.heappop(fre)
                    heapq.heappush(
                        fre,
                        (val,key)
                        )
            iter +=1
        return [y for x,y in fre]


        