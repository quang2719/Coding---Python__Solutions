class MyStack:
    
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.insert(0,x)

    def pop(self) -> int:
        val = 0
        while self.q1:
            if len(self.q1) ==1:
                val = self.q1.pop()
                break
            self.q2.insert(0,self.q1.pop())
        while self.q2:
            self.q1.insert(0,self.q2.pop())
        return val
        

    def top(self) -> int:
        val = 0
        while self.q1:
            if len(self.q1) ==1:
                val = self.q1.pop()
                self.q2.insert(0,val)
                break
            self.q2.insert(0,self.q1.pop())
        while self.q2:
            self.q1.insert(0,self.q2.pop())
        return val

    def empty(self) -> bool:
        return not self.q1

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty() 