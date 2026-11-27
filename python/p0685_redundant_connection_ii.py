class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        incoming = [-1] * (n + 1)
        earlier = later = -1
        for index, (_, child) in enumerate(edges):
            if incoming[child] >= 0:
                earlier, later = incoming[child], index
            else:
                incoming[child] = index
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for index, (source, target) in enumerate(edges):
            if index == later:
                continue
            first, second = find(source), find(target)
            if first == second:
                return edges[earlier if earlier >= 0 else index][:]
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]
        return edges[later][:]
