class CircularQueue:
    def __init__(self, size):
        self.maxSize = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queueArray[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.maxSize
            if self.rear == self.front:
                print("Queue is full. Cannot enqueue.")
                self.rear = (self.rear - 1 + self.maxSize) % self.maxSize
            else:
                self.queueArray[self.rear] = item

    def dequeue(self):
        item = -1  # Assuming -1 represents an empty value

        if not self.isEmpty():
            item = self.queueArray[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.maxSize
        else:
            print("Queue is empty. Cannot dequeue.")

        return item

    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty. No peek value.")
            return -1  # Assuming -1 represents an empty value

    def isEmpty(self):
        return self.front == -1 and self.rear == -1


if __name__ == "__main__":
    circularQueue = CircularQueue(5)

    circularQueue.enqueue(1)
    circularQueue.enqueue(2)
    circularQueue.enqueue(3)

    # Should print 1
    print("Peek:", circularQueue.peek())

    # Should print 1
    print("Dequeue:", circularQueue.dequeue())

    # Should print 2
    print("Peek after dequeue:", circularQueue.peek())
