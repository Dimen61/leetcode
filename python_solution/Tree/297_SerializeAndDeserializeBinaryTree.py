# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Use level-order traversal to serialize tree.
# Time out.
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        seq = ''
        level = [root]
        
        while level:
            next_level = []
            flag = False
            for node in level:
                if node is None:
                    next_level.extend([None, None])
                    seq += '#'
                else:
                    next_level.extend([node.left, node.right])
                    seq += str(node.val)
                    if node.left or node.right:
                        flag = True
            if flag:
                level = next_level
            else:
                break
            
        return seq
                    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        nodes = []
        for index, c in enumerate(data):
            if c == '#':
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(c)))
                
            parent_index = (index-1) // 2
            if index > 0 and nodes[parent_index]:
                if parent_index*2 + 1 == index:
                    nodes[parent_index].left = nodes[index]
                else:
                    nodes[parent_index].right = nodes[index]

        # print('Finish')        
        return nodes[0]


# Use in-order traversal and pre-order traversal to serialize tree.
# Exists some bugs.
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        in_order_seq = []
        pre_order_seq = []
        def in_order_traversal(root):
            if not root: return

            if root.left:
                in_order_traversal(root.left)
            in_order_seq.append(root.val)
            if root.right:
                in_order_traversal(root.right)

        def pre_order_traversal(root):
            if not root: return

            pre_order_seq.append(root.val)
            if root.left:
                pre_order_traversal(root.left)
            if root.right:
                pre_order_traversal(root.right)

        in_order_traversal(root)
        pre_order_traversal(root)

        # print('in_order_seq:', in_order_seq)
        # print('pre_order_seq:', pre_order_seq)

        return ','.join(map(str, in_order_seq)) + \
               ','.join(map(str, pre_order_seq))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        half_len = len(data) // 2

        in_order_seq = list(map(int, data[:half_len].split(',')))
        pre_order_seq = list(map(int, data[half_len:].split(',')))

        assert len(in_order_seq) == len(pre_order_seq)

        def build_tree(seq1, seq2):
            if not seq1:
                return None

            root = TreeNode(seq2[0])
            root_index = seq1.index(seq2[0])
            left = build_tree(seq1[:root_index], seq2[1:1+root_index])
            right = build_tree(seq1[root_index+1:], seq2[1+root_index:])
            root.left = left
            root.right = right

            return root

        return build_tree(in_order_seq, pre_order_seq)

# Using pre-order traversal and recording the null node.
class Codec3:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        seq = []
        def pre_order_traversal(root):
            if not root:
                seq.append('#')
                return
            seq.append(str(root.val))
            pre_order_traversal(root.left)
            pre_order_traversal(root.right)
            
        pre_order_traversal(root)
        return ' '.join(seq)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        seq = data.split()
        vals = iter(seq)
        
        def build_tree():
            val = next(vals)
            if val == '#':
                return None
            else:
                root = TreeNode(int(val))
                root.left = build_tree()
                root.right = build_tree()
                return root
        
        return build_tree()


# Your Codec object will be instantiated and called as such:
node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2
root = node1

def print_tree(root):
    level = [root]

    num = 0

    while level:

        num += 1
        if num == 10: break

        next_level = []
        for node in level:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
        print(' '.join([str(node.val) for node in level if node]))
        level = next_level




codec = Codec2()
seq = codec.serialize(root)
print('seq:', seq)
print('Finish serialize...')
print_tree(codec.deserialize(seq))
print('Finish deserialize...')
























