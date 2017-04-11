# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):

#     def __init__(self, item):
#         self._item = item

#     def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#        return type(self._item) == int

#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#         if self.isInteger():
#             return self._item
#         else:
#             return None

#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """
#         if self.isInteger():
#             return None
#         else:
#             return self._item

# straight solution 
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.current_lst = self.flatten_lst(nestedList)
        self.index = 0

    def flatten_lst(self, nestedList):
        """
        :rtype: List[int]
        """
        if not nestedList: return []
        
        res = []
        for item in nestedList:
            if item.isInteger():
                res.append(item.getInteger())
            else:
                res += (self.flatten_lst(item.getList()))
                print('lst:', item.getList())
                
        return res
        

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.current_lst[self.index-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.current_lst)
        

# Use python generator
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def gen(nestedList):
            for item in nestedList:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    for item2 in gen(item.getList()):
                        yield item2
                        
        self.gen = gen(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.val

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.val = next(self.gen)
            return True
        except StopIteration:
            return False
        

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.val
                    
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            node = self.stack.pop()
            if node.isInteger():
                self.val = node.getInteger()
                return True
            else:
                self.stack.extend([item for item in node.getList()][::-1])
        
        return False
        