class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        edges = [(cost, 0, house) for house, cost in enumerate(wells, 1)]
        edges.extend((cost, first, second) for first, second, cost in pipes)
        edges.sort()
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(house):
            while house != parent[house]:
                parent[house] = parent[parent[house]]
                house = parent[house]
            return house

        answer, needed = 0, n
        for cost, first, second in edges:
            first, second = find(first), find(second)
            if first == second:
                continue
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]
            answer += cost
            needed -= 1
            if needed == 0:
                return answer
