# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        # if root.val > sum: return False    
        
        if not root.left and not root.right:
            return sum == root.val
        else:
            if root.left:
                if self.hasPathSum(root.left, sum-root.val):
                    return True
            if root.right:
                if self.hasPathSum(root.right, sum-root.val):
                    return True
            
            return False
        

a = Solution()
node0 = TreeNode(-2)
node1 = TreeNode(-3)
node0.right = node1
print(a.hasPathSum(node0, -5))