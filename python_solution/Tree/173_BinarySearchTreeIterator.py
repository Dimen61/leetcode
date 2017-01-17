# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    """
    Recursion to implement in-ordered traversal.
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        
        def in_ordered_traversal(root):
            if not root: return
            in_ordered_traversal(root.left)    
            self.vals.append(root.val)
            in_ordered_traversal(root.right)
        
        in_ordered_traversal(root)
        self.count = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count < len(self.vals)
        

    def next(self):
        """
        :rtype: int
        """
        val = self.vals[self.count]
        self.count += 1
        return val
        

class BSTIterator(object):
    """
    Implement in-ordered traversal iteratively.
    The best way to solve the problem.
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node_stack = []
        self.cur_node = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_node or self.node_stack
        

    def next(self):
        """
        :rtype: int
        """
        while self.cur_node:
            # prev_node = self.cur_node
            self.node_stack.append(self.cur_node)
            self.cur_node = self.cur_node.left
        node = self.node_stack.pop()
        self.cur_node = node.right
        return node.val

def in_order_traversal(root):
    node_stack = []
    cur_node = root
    path = []

    while cur_node or node_stack:
        while cur_node:
            node_stack.append(cur_node)
            cur_node = cur_node.left
        node = node_stack.pop()
        cur_node = node.right
        path.append(node.val)

    return path





# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

















