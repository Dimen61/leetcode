# Just using queue to implement stack.
class Queue(object):
    
    def __init__(self):
        self.lst = []
        
    def is_empty(self):
        return len(self.lst) == 0
        
    def push(self, x):
        self.lst.append(x)
        
    def pop(self):
        return self.lst.pop(0)
        
    def size(self):
        return len(self.lst)

    def peek(self):
        return self.lst[0]
    
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        length = self.queue.size()
        self.queue.push(x)

        for i in range(length):
            self.queue.push(self.queue.pop())

        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue.peek()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.is_empty()