# Tree

Tree is a kind of directed graph. We could define it recursionly:

1. A node is a tree.
2. serveral trees and a node which exclude from the trees compose a tree.

Properties:
* If there are n nodes, there are n-1 edges.

## Binary Tree
A tree which only has at most two subtrees for any nodes is binary tree.

Properities:
* There are n nodes which have two children in binary tree. It would infer to there are n+1 leaves which have no child.(It could be proofed by induction)
* Given n nodes, the number of different binary trees could be constructed is the [catalan number](https://en.wikipedia.org/wiki/Catalan_number).  h(n)=C(2*n，n)/(n+1).

