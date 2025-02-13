import heapq
ar = [1,2,4,5,6,4,23]
heap = []
for x in ar:
    heapq.heappush(heap,x)
while heap:
    print(heapq.heappop(heap))