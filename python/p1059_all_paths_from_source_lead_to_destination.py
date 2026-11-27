class Solution:
    def leadsToDestination(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]
        for first,second in edges:
            graph[first].append(second)
        if graph[destination]:
            return False
        state = [0] * n
        state[source] = 1
        stack = [(source,0)]
        while stack:
            node,next_edge = stack[-1]
            if not graph[node]:
                if node != destination:
                    return False
                state[node] = 2
                stack.pop()
                continue
            if next_edge == len(graph[node]):
                state[node] = 2
                stack.pop()
                continue
            following = graph[node][next_edge]
            stack[-1] = node,next_edge + 1
            if state[following] == 1:
                return False
            if state[following] == 0:
                state[following] = 1
                stack.append((following,0))
        return True
