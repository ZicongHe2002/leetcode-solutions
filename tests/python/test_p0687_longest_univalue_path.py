import unittest
from collections import deque
from functools import lru_cache
from itertools import product

from python.p0687_longest_univalue_path import Solution


class Node:
    __hash__ = None

    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size)
                 for left in shapes(count) for right in shapes(size - count - 1))


def build(shape, values):
    if shape is None:
        return None
    node = Node(next(values))
    node.left, node.right = build(shape[0], values), build(shape[1], values)
    return node


def original_nodes(root):
    nodes, pending = [], [root] if root is not None else []
    while pending:
        node = pending.pop()
        nodes.append(node)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return nodes


def equal_value_graph(root):
    nodes = original_nodes(root)
    graph = {id(node): [] for node in nodes}
    for node in nodes:
        for child in (node.left, node.right):
            if child is not None and child.val == node.val:
                graph[id(node)].append(id(child))
                graph[id(child)].append(id(node))
    return graph


def distances(graph, start):
    result, pending = {start: 0}, deque([start])
    while pending:
        node = pending.popleft()
        for neighbour in graph[node]:
            if neighbour not in result:
                result[neighbour] = result[node] + 1
                pending.append(neighbour)
    return result


def graph_diameter(root, large=False):
    graph = equal_value_graph(root)
    if not large:
        return max((max(distances(graph, node).values()) for node in graph), default=0)
    remaining, best = set(graph), 0
    while remaining:
        reached = distances(graph, next(iter(remaining)))
        endpoint = max(reached, key=reached.get)
        best = max(best, max(distances(graph, endpoint).values()))
        remaining.difference_update(reached)
    return best


class LongestUnivaluePathTests(unittest.TestCase):
    def check(self, root, large=False, expected=None):
        before = [(node, node.val, node.left, node.right) for node in original_nodes(root)]
        if expected is None:
            expected = graph_diameter(root, large)
        result = Solution().longestUnivaluePath(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_shapes_and_signed_labels_against_all_graph_distances(self):
        checked = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product((-1000, 0, 1000), repeat=size):
                    self.check(build(shape, iter(values)))
                    checked += 1
        self.assertEqual(checked, 11497)

    def test_ten_thousand_nodes_depth_one_thousand_and_path_below_root(self):
        nodes = [Node(1) for _ in range(10000)]
        for i, node in enumerate(nodes):
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
        self.check(nodes[0], large=True)
        nodes[0].val = 0
        self.check(nodes[0], large=True)
        for alternating in (False, True):
            chain = None
            for i in range(1000):
                chain = Node(i % 2 if alternating else -1000, chain)
            self.check(chain, large=True, expected=0 if alternating else 999)
        root = Node(5)
        for side in ('left', 'right'):
            node = root
            for _ in range(999):
                child = Node(5)
                setattr(node, side, child)
                node = child
        self.check(root, large=True, expected=1998)


if __name__ == '__main__':
    unittest.main()
