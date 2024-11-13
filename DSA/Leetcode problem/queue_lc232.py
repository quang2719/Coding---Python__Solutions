class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []    

        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return val

    def peek(self) -> int:
        if self.empty():
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        self.stack1.append(val)
        while self.stack2:
            self.stack1.append( self.stack2.pop())
        return val

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()