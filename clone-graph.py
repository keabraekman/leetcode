# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


    
def cloneGraph(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node) if node else None


def clonegraph(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in copy.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    if node:
        return dfs(node)
    else:
        None







class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



def cloneGraph(node):
    oldNew = {}
    def dfs(node):
        if node in oldNew:
            return oldNew[node]
        copy = Node(node.val)
        oldNew[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(dfs(n))
        return copy
    if node:
        return dfs(node)
    else:
        return None