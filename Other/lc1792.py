import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        res = 0
        id = 0
        for p,t in classes:
            delta = float(p+1)/float(t+1)-float(p)/float(t)
            heapq.heappush(
                heap, 
                (-delta,id,p,t)
                )
            id+=1
        while extraStudents:
            delta,_,p,t = heapq.heappop(heap)
            #choose p,t
            p+=1
            t+=1
            new_delta = float(p+1)/float(t+1)-float(p)/float(t)
            heapq.heappush(
                heap, 
                (-new_delta,id,p,t)
                )
            id+=1
            extraStudents -= 1
        while heap:
            delta,_,p,t = heapq.heappop(heap)
            res += float(p)/float(t)
        return res/float(len(classes))
