from collections import deque


class Solution:
    def sortItems(self, n, m, group, beforeItems):
        groups = list(group)
        for item in range(n):
            if groups[item] == -1:
                groups[item] = m
                m += 1
        item_edges = [[] for _ in range(n)]
        item_degree = [0] * n
        group_edges = [set() for _ in range(m)]
        group_degree = [0] * m
        for item, dependencies in enumerate(beforeItems):
            for previous in dependencies:
                item_edges[previous].append(item)
                item_degree[item] += 1
                source, target = groups[previous], groups[item]
                if source != target and target not in group_edges[source]:
                    group_edges[source].add(target)
                    group_degree[target] += 1

        def topological(edges, degree):
            pending = deque(index for index, count in enumerate(degree) if count == 0)
            result = []
            while pending:
                node = pending.popleft()
                result.append(node)
                for following in edges[node]:
                    degree[following] -= 1
                    if degree[following] == 0:
                        pending.append(following)
            return result

        items = topological(item_edges, item_degree)
        order = topological(group_edges, group_degree)
        if len(items) != n or len(order) != m:
            return []
        buckets = [[] for _ in range(m)]
        for item in items:
            buckets[groups[item]].append(item)
        return [item for identity in order for item in buckets[identity]]
