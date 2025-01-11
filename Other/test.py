import heapq

hp = []
nums = [1,2,3,6,45,78]
for x in nums:
    heapq.heappush(hp,x)
while hp:
    print(heapq.heappop(hp))
