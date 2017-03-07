class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_d = []
        self.stack_m = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack_d.append(x)
        
        if not self.stack_m or x <= self.getMin():
            self.stack_m.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack_d.pop()
        if x == self.getMin():
            self.stack_m.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack_d[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()