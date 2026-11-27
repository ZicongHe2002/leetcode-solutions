class Solution:
    def removeStones(self, stones):
        parent = {}
        sizes = {}

        def find(node):
            if node not in parent:
                parent[node] = node
                sizes[node] = 1
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for row,column in stones:
            first,second = find(('r',row)),find(('c',column))
            if first != second:
                if sizes[first] < sizes[second]:
                    first,second = second,first
                parent[second] = first
                sizes[first] += sizes[second]
        components = len({find(('r',row)) for row,_ in stones})
        return len(stones) - components
