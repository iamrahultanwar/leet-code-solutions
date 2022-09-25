class Node:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.next = nextNode
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k # maximum number elements 
        self.head = None
        self.tail = None
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        
        if self.isFull(): return False
        
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        
        self.count += 1
        
        return True
        

    def deQueue(self) -> bool:
        
        if self.isEmpty(): return False
        
        self.head = self.head.next
        self.count -= 1
        
        return True
        

    def Front(self) -> int:
        
        if self.isEmpty(): return -1
        
        return self.head.value
        

    def Rear(self) -> int:
        
        if self.isEmpty(): return -1
        
        return self.tail.value

    def isEmpty(self) -> bool:
        
        return self.count == 0

    def isFull(self) -> bool:
        
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()