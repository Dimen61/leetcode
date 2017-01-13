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
        The most benift from this problem is that the order of organize sub
        recursion is also important to the rightness of solution.
        """
        if not root: return 
    
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.first_next_child(root.next)
            
        next_right_node = self.first_next_child(root.next)
        if root.right and next_right_node:
            root.right.next = next_right_node

        # We must recurion the right part first, because
        # the process of the recursion of the left part, perhaps 
        # needs the result of the right part.
        self.connect(root.right)            
        self.connect(root.left)
        
    def first_next_child(self, root):
        if not root: return None
        if root.left:
            return root.left
        elif root.right:
            return root.right
        else:
            return self.first_next_child(root.next)




nodeA = TreeLinkNode(2)
nodeB = TreeLinkNode(1)
nodeC = TreeLinkNode(3)
nodeD = TreeLinkNode(0)
nodeE = TreeLinkNode(7)
nodeF = TreeLinkNode(9)
nodeG = TreeLinkNode(1)
nodeH = TreeLinkNode(2)
nodeI = TreeLinkNode(1)
nodeJ = TreeLinkNode(0)
nodeK = TreeLinkNode(8)
nodeL = TreeLinkNode(8)
nodeM = TreeLinkNode(7)

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.left = nodeF
nodeC.right = nodeG
nodeD.left = nodeH
nodeE.left = nodeI
nodeE.right = nodeJ
nodeG.left = nodeK
nodeG.right = nodeL
nodeJ.left = nodeM

a = Solution()
a.connect(nodeA)

# Ouput
root = nodeA
while root:
    node = root
    informs = []
    while node:
        informs.append(node.val)
        node = node.next
    print(informs)
    root = root.left

# print('*' * 20)
# print('Test first_next_child')
# print('-'*10)
# # print(a.first_next_child(nodeE.next).val)
# print('A:', a.first_next_child(nodeA).val)
# print('B:', a.first_next_child(nodeB).val)
# print('C: ', a.first_next_child(nodeC).val)
# print('D: ', a.first_next_child(nodeD).val)
# print('E: ', a.first_next_child(nodeE).val)
# print('F: ', a.first_next_child(nodeF).val)
# print('G: ', a.first_next_child(nodeG).val)
# print('H: ', a.first_next_child(nodeH).val)
# print('I: ', a.first_next_child(nodeI).val)
# print('J: ', a.first_next_child(nodeJ).val)
# print('K: ', a.first_next_child(nodeK))
# print('L: ', a.first_next_child(nodeL))
# print('M: ', a.first_next_child(nodeM))


# print(nodeJ.next)
print('*' * 20)
# print(nodeF.next.val)