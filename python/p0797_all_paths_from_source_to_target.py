class Solution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        paths = []
        current = [0]

        def visit(node):
            if node == target:
                paths.append(current[:])
                return
            for successor in graph[node]:
                current.append(successor)
                visit(successor)
                current.pop()

        visit(0)
        return paths
