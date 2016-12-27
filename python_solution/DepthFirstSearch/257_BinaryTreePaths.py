# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        paths = []
        
        def dfs(node, path):
            if not node: 
                paths.append(path)
                return
            
            new_path = str(node.val) if not path else path+'->'+str(node.val)
            if node.left:
                dfs(node.left, new_path)
            if node.right:
                dfs(node.right, new_path)
            if not node.left and not node.right:
                dfs(None, new_path)
        
        dfs(root, '')
        return paths
        