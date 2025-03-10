class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = {}
        for i in range(right+1):
            if i >= 2:
                isPrime[i] = True
            else: isPrime[i] = False
        res = []
        for i in range(right+1):
            if isPrime[i]:
                j = i*i
                while j<= right:
                    isPrime[j] = False
                    j+=i
                if i >= left:
                    res.append(i)
        if len(res) < 2:
            return [-1,-1]
        
        pair = [res[0],res[1]]
        for i in range(len(res)-1):
            if res[i+1] - res[i] < pair[1]-pair[0]:
                pair[1] = res[i+1]
                pair[0] = res[i]
        return pair
        
        
                