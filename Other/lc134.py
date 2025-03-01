class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        lost = []
        for i in range(len(cost)):
            if i == len(cost)-1:
                lost.append(gas[0]-cost[i])
            else:
                lost.append(gas[i+1]-cost[i])
        