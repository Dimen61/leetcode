# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        seq = []
        stack = [(root, False)]
        
        while stack:
            node, flag = stack.pop()
            if not node: continue
            
            if flag:
                seq.append(node.val)
                if node.right:
                    stack.append((node.right, False))
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                    
        return seq

class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        seq = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                seq.append(node.val)
                root = node.right                

        return seq

a = Solution1()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3

print(a.inorderTraversal(t1))























