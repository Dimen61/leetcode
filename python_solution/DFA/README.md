# DFA(Deterministic Finite Automation)

## Definition

DFA is a directed graph which contains nodes and directed edges. There are three kinds of nodes which are begin nodes, middle nodes and final nodes. Edges have some value which bring the stage from begin node to end node. DFA could be used to determined the **string** is valid or not. Of course, we could abstract many things into strings. The process below:

1. We begin at the begin nodes as current stage.
2. When we sweep the string, we use the same value of edge and the same begin node as current stage, then we get the new stage as the end node of the edge.
3. If our stage could stop at the node which is final node, the string is valid. Otherwisse, the string is invalid.

## Application

We could use the idea of DFA to determine the string valid or not. And we could use the **dict** data structure in Python to implement DFA's graph.