**Backtracking** is an algorithm to find all solutions of [constraint satisfaction problem](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem).

It use [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) to construct a search tree from the root down to generate possible solutions. Each node in the tree represents a state which is possible a soluiton.

Hence, the key of backtracking is how to define:

*	Node (how to represent state)
*	How to generate child from current node (how to get possible solution)
*	Judge whether the node belongs to solutions
*	Prune the node if it could not construct a full solution.