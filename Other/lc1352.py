class ProductOfNumbers(object):

    def __init__(self):
        self.arr = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr.append(num)
        self.cache = {}
        self.maxPreK = 0
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k <= self.maxPreK:
            return self.cache[k]
        
        res = (self.cache[self.maxPreK] if self.maxPreK != 0 else 1)
        for id in range(self.maxPreK+1,k+1):
            res*= self.arr[len(self.arr) -id]
            self.cache[id] = res
            
            self.maxPreK = k
        return res
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)