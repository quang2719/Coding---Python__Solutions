from queue import Queue
class List:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = -1
        self.rear  = -1
        self.q = [0]*k
        self.size = k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.q[self.rear] = value
            return True

        else:
            self.rear = (self.rear+1)%self.size
            self.q[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
                return True
            self.front = (self.front+1)%self.size
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == (self.rear +1)%self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()