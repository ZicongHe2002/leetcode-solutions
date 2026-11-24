import unittest
from itertools import combinations

from python.p0133_clone_graph import Node, Solution


def adjacency(size, edges):
    graph = [[] for _ in range(size)]
    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)
    return graph


def connected(graph):
    visited = {0}
    pending = [0]
    while pending:
        for neighbor in graph[pending.pop()]:
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)
    return len(visited) == len(graph)


class CloneGraphTests(unittest.TestCase):
    def check(self, graph, start):
        nodes = [Node(index + 1) for index in range(len(graph))]
        for index, neighbors in enumerate(graph):
            nodes[index].neighbors = [nodes[neighbor] for neighbor in neighbors]
        originals = {id(node) for node in nodes}
        lists = [node.neighbors for node in nodes]
        result = Solution().cloneGraph(nodes[start])
        self.assertEqual(result.val, start + 1)
        by_label, visited, pending = {}, set(), [result]
        while pending:
            clone = pending.pop()
            if id(clone) in visited:
                continue
            self.assertNotIn(id(clone), originals)
            self.assertNotIn(clone.val, by_label)
            by_label[clone.val] = clone
            visited.add(id(clone))
            pending.extend(clone.neighbors)
        self.assertEqual(set(by_label), set(range(1, len(nodes) + 1)))
        for index, neighbors in enumerate(graph):
            clone = by_label[index + 1]
            self.assertEqual([node.val for node in clone.neighbors], [neighbor + 1 for neighbor in neighbors])
            for neighbor, copied in zip(neighbors, clone.neighbors):
                self.assertIs(copied, by_label[neighbor + 1])
        result.val = -1
        result.neighbors.clear()
        for index, neighbors in enumerate(graph):
            self.assertEqual(nodes[index].val, index + 1)
            self.assertIs(nodes[index].neighbors, lists[index])
            self.assertEqual(len(nodes[index].neighbors), len(neighbors))
            for neighbor, original in zip(neighbors, nodes[index].neighbors):
                self.assertIs(original, nodes[neighbor])

    def test_all_small_connected_graphs_and_entries_against_adjacency_labels(self):
        graphs = checks = 0
        for size in range(1, 6):
            possible = list(combinations(range(size), 2))
            for mask in range(1 << len(possible)):
                graph = adjacency(size, [edge for bit, edge in enumerate(possible) if mask & (1 << bit)])
                if not connected(graph):
                    continue
                graphs += 1
                for start in range(size):
                    self.check(graph, start)
                    checks += 1
        self.assertEqual((graphs, checks), (772, 3807))

    def test_maximum_chain_complete_graph_singleton_and_empty(self):
        self.check(adjacency(100, [(index, index + 1) for index in range(99)]), 49)
        self.check(adjacency(100, list(combinations(range(100), 2))), 99)
        self.check([[]], 0)
        self.assertIsNone(Solution().cloneGraph(None))


if __name__ == '__main__':
    unittest.main()
