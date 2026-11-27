import unittest

from python.p0841_keys_and_rooms import Solution


def all_rooms_by_closure(rooms):
    reach = [[False] * len(rooms) for _ in rooms]
    for room, keys in enumerate(rooms):
        reach[room][room] = True
        for key in keys:
            reach[room][key] = True
    for middle in range(len(rooms)):
        for first in range(len(rooms)):
            for second in range(len(rooms)):
                reach[first][second] |= reach[first][middle] and reach[middle][second]
    return all(reach[0])


class RoomKeysTests(unittest.TestCase):
    def check(self, rooms, expected=None):
        self.assertTrue(1 <= sum(map(len, rooms)) <= 3000)
        before = [keys[:] for keys in rooms]
        if expected is None:
            expected = all_rooms_by_closure(rooms)
        result = Solution().canVisitAllRooms(rooms)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(rooms, before)

    def test_every_small_nonempty_directed_graph_against_closure(self):
        checks = 0
        for size in range(2, 5):
            edges = [(first, second) for first in range(size) for second in range(size)]
            for mask in range(1, 1 << len(edges)):
                rooms = [[] for _ in range(size)]
                for index, (first, second) in enumerate(edges):
                    if mask >> index & 1:
                        rooms[first].append(second)
                self.check(rooms)
                checks += 1
        self.assertEqual(checks, 66061)

    def test_maximum_rooms_keys_chains_cycles_and_unreachable_component(self):
        self.check([[room + 1] for room in range(999)] + [[]], True)
        self.check([[(room + 1) % 1000] for room in range(1000)], True)
        self.check([[(room + shift) % 1000 for shift in (1, 2, 3)] for room in range(1000)], True)
        separated = [[1], []] + [[room + 1] for room in range(2, 999)] + [[]]
        self.assertEqual(len(separated), 1000)
        self.check(separated, False)


if __name__ == '__main__':
    unittest.main()
