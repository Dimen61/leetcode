# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []

        def get_roots(start, end):
            roots = []
            if start == end:
                return [TreeNode(start)]
            elif start > end:
                return []
            else:
                for i in range(start, end+1):
                    left_roots = get_roots(start, i-1) 
                    right_roots = get_roots(i+1, end)

                    if not left_roots:
                        for right_root in right_roots:
                            root = TreeNode(i)
                            root.left = None
                            root.right = right_root
                            roots.append(root)
                    elif not right_roots:
                        for left_root in left_roots:
                            root = TreeNode(i)
                            root.right = None
                            root.left = left_root
                            roots.append(root)
                    else:
                        for left_root in left_roots:
                            for right_root in right_roots:
                                root = TreeNode(i)
                                root.left = left_root
                                root.right = right_root
                                roots.append(root)
            return roots

        return get_roots(1, n)