import collections
class LRUCache(object):
    '''
    Using collections.OrderedDict.
    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(False)
        self.cache[key] = value
            

class Node(object):

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if node == self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:         # Only one node in double linked list
                self.head = self.tail = None
        elif node == self.tail:
            self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = node.next = None


class LRUCache(object):
    '''
    Using double linked list.    
    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.double_linked_list = DoubleLinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.double_linked_list.remove(node)
            self.double_linked_list.append(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            node = self.cache[key]
            self.double_linked_list.remove(node)
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.double_linked_list.append(new_node)
        elif len(self.cache) == self.capacity:
            node = self.double_linked_list.head
            self.cache.pop(node.key)
            self.double_linked_list.remove(node)
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.double_linked_list.append(new_node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.double_linked_list.append(node)

# 2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]
        
cache = LRUCache(2)
cache.set(2, 1)
cache.set(2, 2)
print(cache.get(2))
cache.set(1, 1)
cache.set(4, 1)
print(cache.get(2))
















