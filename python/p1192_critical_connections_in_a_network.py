class Solution:
    def criticalConnections(self, n, connections):
        edges = [[] for _ in range(n)]
        for identity, (first, second) in enumerate(connections):
            edges[first].append((second, identity))
            edges[second].append((first, identity))
        discovered = [-1] * n
        low = [0] * n
        clock = 0
        answer = []
        for root in range(n):
            if discovered[root] >= 0:
                continue
            discovered[root] = low[root] = clock
            clock += 1
            stack = [(root, -1, -1, iter(edges[root]))]
            while stack:
                node, parent, parent_edge, following = stack[-1]
                try:
                    other, identity = next(following)
                except StopIteration:
                    stack.pop()
                    if parent >= 0:
                        if low[node] > discovered[parent]:
                            answer.append([parent, node])
                        low[parent] = min(low[parent], low[node])
                    continue
                if identity == parent_edge:
                    continue
                if discovered[other] < 0:
                    discovered[other] = low[other] = clock
                    clock += 1
                    stack.append((other, node, identity, iter(edges[other])))
                else:
                    low[node] = min(low[node], discovered[other])
        return answer
