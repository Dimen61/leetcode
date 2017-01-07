# Depth-first Search

Depth-first search is an algorithm for traversal tree of graph. If the object is graph, we regard the graph as root by treating the first visited node as root. Another traversal algorithm is [BFS](https://github.com/Dimen61/leetcode/tree/Combination/python_solution/BreadthFirstSearch). The difference between DFS and BFS is that DFS prefer to visit the next level  nodes in the tree than the same level of nodes except that there is not next level then backtrack to the visited node which could get unvisited next level nodes, then go to the next level.

## Time Complexity
Traverse an entire graph takes O(|V|+|E|), the same as BFS.

## Space Complexity
For visiting node at most once application, it takes O(|V|) at worst case, the same as BFS.

## Iterative Deepening Depth-first Search
For application in artificial intelligence or web-crawling, using the DFS to traverse is non-terminated because of unlimited or large enough graph. To make our program finally stop, we always limit the depth of DFS. However, some nodes or solution which we want may be deeper than the depth we set. Hence, we try the limited depth increasing, once find the solution, we stop. From the format view, it seems like that a DFS in a loop. This is iterative deepening depth-first search. The same space complexity as DFS, while time complexity is the final depth(alway be regard as constant) time DFS.

## Pseudocode
Implement with recursion


```python
def dfs(G, node):
    # Do something with current node.
	visit[node] = True
    for next_node in adj_nodes(node):
        if not visit[node]:
            dfs(G, next_node)
    
```

Implement with stack

```python
def dfs(G, node):
	nodes = stack()
	nodes.push(node)
    
	while not nodes.empty():
        node = node.pop()
        # Do something with current node.
        visit[node] = True
        for next_node in adj_nodes(node):
            if not visit[next_node]:
                nodes.push(next_node)
```
