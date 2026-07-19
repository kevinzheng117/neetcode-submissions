class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = dict()

        def getNode(val):
            if val not in nodes:
                nodes[val] = Node(val)
            return nodes[val]
        
        def find(node):
            if node != node.parent:
                node.parent = find(node.parent)
            return node.parent
        
        def union(val1, val2):
            node1, node2 = getNode(val1), getNode(val2)

            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return False
            elif root1.size > root2.size:
                root2.parent = root1
                root1.size += root2.size
            else:
                root1.parent = root2
                root2.size += root1.size
            
            return True
        
        for val1, val2 in edges:
            if not union(val1, val2):
                return [val1, val2]
        
        return True
