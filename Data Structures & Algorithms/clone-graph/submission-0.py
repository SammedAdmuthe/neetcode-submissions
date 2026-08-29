"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        new_node = Node()
        seen = set()
        old_new = {}
        head = node
        def dfs(node):
            
            if node in seen:
                return

            if node not in old_new:
                old_new[node] = Node(node.val)

            seen.add(node)
            for neigh in node.neighbors:
                if neigh not in old_new:
                    old_new[neigh] = Node(neigh.val)
                old_new[node].neighbors.append(old_new[neigh])
                dfs(neigh)
        
        dfs(node)
        print(old_new[head].neighbors)
        return old_new[head]