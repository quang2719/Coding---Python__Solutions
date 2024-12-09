class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries)):
            if i == len(timeSeries)-1: 
                total += duration
                break
            t = timeSeries[i]
            t2 = timeSeries[i+1]
            if t + duration-1 >= t2:
                total += (t2 - t)
            else: total += duration
        return total