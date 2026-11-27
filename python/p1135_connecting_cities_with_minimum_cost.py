class Solution:
    def minimumCost(self, n, connections):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(city):
            while city != parent[city]:
                parent[city] = parent[parent[city]]
                city = parent[city]
            return city

        groups, cost = n, 0
        for first, second, price in sorted(connections, key=lambda edge: edge[2]):
            first, second = find(first), find(second)
            if first == second:
                continue
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]
            groups -= 1
            cost += price
        return cost if groups == 1 else -1
