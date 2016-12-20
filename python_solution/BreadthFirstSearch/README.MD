## Breadth First Search
### Basic Idea

We use **breadth first search** to traversal the tree in the way:

* Traversal the neighborhoods of the node before visiting the next level of the tree.

If the given is a graph, we regard the certain node as the root of the tree and do above.

### Completeness
If the given graph is infinite , such as AI application, and our goal is just one solution in the graph. BFS could find one solution, while DFS could not get a possible solution at all.