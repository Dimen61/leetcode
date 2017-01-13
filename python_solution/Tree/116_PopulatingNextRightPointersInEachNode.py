# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        Using the coding of binary tree to find the next node in the tree.
        """

        if not root: return
        
        def get_height(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height
        
        def get_node(s):
            if not s: return root
            node = root
            for c in s:
                if c == '0':
                    node = node.left
                elif c == '1':
                    node = node.right
            return node
            
        height = get_height(root)
        # print('height:', height)
        for length in range(height):
            if length == 0:
                root.next = None
            else:
                nodes = []
                print('length:',length)
                for num in range(2 ** length):
                    s = bin(num)[2:]
                    s = '0' * (length - len(s)) + s
                    print('s:', s)
                    nodes.append(get_node(s))
                # print('nodes size:', len(nodes))
                print([node.val for node in nodes])
                for i in range(len(nodes)):
                    if i < len(nodes) - 1:
                        nodes[i].next = nodes[i+1]
                    else:
                        nodes[i].next = None


class Solution2(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        Recursion implement which uses the properties of perfect tree.
        """
        if not root: return

        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)


                        
                        
a = Solution()
node1 = TreeLinkNode('Root')
node2 = TreeLinkNode('0')
node3 = TreeLinkNode('1')
node4 = TreeLinkNode('00')
node5 = TreeLinkNode('01')
node6 = TreeLinkNode('10')
node7 = TreeLinkNode('11')

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


a.connect(node1)

# Ouput
root = node1
while root:
    node = root
    informs = []
    while node:
        informs.append(node.val)
        node = node.next
    print(informs)
    root = root.left





















