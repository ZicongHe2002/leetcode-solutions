class Solution:
    def sumOfDistancesInTree(self, n, edges):
        neighbors = [[] for _ in range(n)]
        for first,second in edges:
            neighbors[first].append(second)
            neighbors[second].append(first)
        parent = [-1] * n
        parent[0] = 0
        depth = [0] * n
        order = [0]
        for node in order:
            for following in neighbors[node]:
                if following != parent[node]:
                    parent[following] = node
                    depth[following] = depth[node] + 1
                    order.append(following)
        subtree = [1] * n
        for node in reversed(order[1:]):
            subtree[parent[node]] += subtree[node]
        answer = [0] * n
        answer[0] = sum(depth)
        for node in order[1:]:
            answer[node] = answer[parent[node]] + n - 2 * subtree[node]
        return answer
