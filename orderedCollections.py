import heapq

class Stack:
    """Implements a stack data structure"""
    def __init__(self):
        self.list = []

    def push(self, item):
        """Pushes input item on top of the stack"""
        self.list.append(item)

    def pop(self):
        """Pops off the item on top of the stack and returns it"""
        return self.list.pop()

    def isEmpty(self):
        """Returns true if the stack is empty, false otherwise"""
        return len(self.list) == 0

class Queue:
    """Implements a FIFO queue data structure"""
    def __init__(self):
        self.list = []

    def push(self, item):
        """Places input item to the end of the queue"""
        self.list.insert(0, item)

    def pop(self):
        """Removes item from front of queue and returns it"""
        return self.list.pop()

    def isEmpty(self):
        """Returns true if the queue is empty, false otherwise"""
        return len(self.list) == 0

class PriorityQueue:
    """Implements a priority queue data structure"""
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Pushes input item to appropriate location in queue, based on priority"""
        entry = (priority, item)
        heapq.heappush(self.heap, entry)

    def pop(self):
        """Removes item from the front of queue and returns it"""
        (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        """Returns true if the queue is empty, false otherwise"""
        return len(self.heap) == 0