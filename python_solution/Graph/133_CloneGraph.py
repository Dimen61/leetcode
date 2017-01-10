# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import collections
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        '''
        Naive BFS
        '''
        if not node: return None
        
        new_node = UndirectedGraphNode(node.label)
        visited_labels = set([node.label])
        label_node_map = { node.label:new_node }
        queue = collections.deque([(node, new_node)])
        first_new_node = new_node
        
        while queue:
            old_node, new_node = queue.popleft()
            for node in old_node.neighbors:
                if node.label not in label_node_map:
                    new_node_nei = UndirectedGraphNode(node.label)
                    label_node_map[node.label] = new_node_nei
                    new_node.neighbors.append(new_node_nei)
                else:
                    new_node_nei = label_node_map[node.label]
                    new_node.neighbors.append(new_node_nei)
                    
                if node.label not in visited_labels:
                    visited_labels.add(node.label)
                    queue.append((node, new_node_nei))
                    
            
        return first_new_node


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        '''
        Concise search implement.

        The basic idea is using a map to maintain a relationship between
        old node and new node. During traversal the old nodes, check the neighbors
        of the current old node, if it is in the map which means we have created a 
        new node for it, so we just add it to neighbors. Otherwise, we have to create
        a new node too.
        '''
        if not node: return None
        old_new_map = {}
        stack = [node]
        new_node = UndirectedGraphNode(node.label)
        old_new_map[node] = new_node
        first_new_node = new_node

        while stack:
            node = stack.pop()
            for adj_node in node.neighbors:
                if adj_node not in old_new_map:
                    stack.append(adj_node)
                    new_node = UndirectedGraphNode(adj_node.label)
                    old_new_map[adj_node] = new_node
                    old_new_map[node].neighbors.append(new_node)
                else:
                    old_new_map[node].neighbors.append(old_new_map[adj_node])

        return first_new_node















