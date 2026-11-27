class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (numerator, denominator), ratio in zip(equations, values):
            graph.setdefault(numerator, []).append((denominator, ratio))
            graph.setdefault(denominator, []).append((numerator, 1.0 / ratio))

        def evaluate(source, destination):
            if source not in graph or destination not in graph:
                return -1.0
            stack, seen = [(source, 1.0)], {source}
            while stack:
                node, product = stack.pop()
                if node == destination:
                    return product
                for neighbor, ratio in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, product * ratio))
            return -1.0

        return [evaluate(source, destination) for source, destination in queries]
