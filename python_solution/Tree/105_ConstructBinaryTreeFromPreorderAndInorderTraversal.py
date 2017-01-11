# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        The key idea is to find the node which splits the tree into left
        child tree and right child tree. And using recursion to implement.

        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        assert len(preorder) == len(inorder)
        if not preorder: return None
        
        node = TreeNode(preorder[0])
        left_len = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:1+left_len], inorder[:left_len])
        node.right = self.buildTree(preorder[1+left_len:], inorder[left_len+1:])
        
        return node

class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        assert len(preorder) == len(inorder)
        if not preorder: return None
        
        n = len(preorder)

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right: return None

            new_node = TreeNode(preorder[pre_left])            
            new_index = inorder.index(preorder[pre_left])
            left_tree_len = new_index - in_left
            new_node.left = helper(pre_left+1, pre_left+left_tree_len, in_left, new_index-1)
            new_node.right = helper(pre_left+left_tree_len+1, pre_right, new_index+1, in_right)

            return new_node

        return helper(0, n-1, 0, n-1)



a = Solution2()
# node = a.buildTree([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3])
node = a.buildTree([1, 2, 3], [1, 2, 3])

level = [node]
while level:
    print([node.val for node in level])
    next_level = []
    for node in level:
        if node.left: next_level.append(node.left)
        if node.right: next_level.append(node.right)
    level = next_level















