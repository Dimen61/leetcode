# Use two stack to simulate a queue
class Stack(object):
    
    def __init__(self):
        self.lst = []
        
    def push(self, x):
        self.lst.append(x)
        
    def pop(self):
        return self.lst.pop()
        
    def top(self):
        return self.lst[-1]
        
    def size(self):
        return len(self.lst)
        
    def is_empty(self):
        return len(self.lst) == 0
        
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = Stack()
        self.output_stack = Stack()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input_stack.push(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.output_stack.is_empty():
            return self.output_stack.pop()
        else:
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
            return self.output_stack.pop()
                

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output_stack.is_empty():
            return self.output_stack.top()
        else:
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
            return self.output_stack.top()
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.output_stack.is_empty() and self.input_stack.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()