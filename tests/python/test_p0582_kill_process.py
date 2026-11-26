from itertools import product
import unittest

from python.p0582_kill_process import Solution


def parent_chain_oracle(pid, ppid, kill):
    parents = dict(zip(pid, ppid))
    answer = set()
    for process in pid:
        ancestor = process
        while ancestor != 0:
            if ancestor == kill:
                answer.add(process)
                break
            ancestor = parents[ancestor]
    return answer


class KillProcessTests(unittest.TestCase):
    def check(self, pid, ppid, kill, expected):
        before = (pid[:], ppid[:])
        result = Solution().killProcess(pid, ppid, kill)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), expected)
        self.assertEqual((pid, ppid), before)

    def test_increasing_parent_trees_relabelled_and_reversed_against_parent_chains(self):
        trees = checks = 0
        for size in range(1, 9):
            labels = [50000 - index for index in range(size)]
            for choices in product(*(range(child) for child in range(1, size))):
                parents = [0] + [labels[parent] for parent in choices]
                pid, ppid = labels[::-1], parents[::-1]
                trees += 1
                for kill in labels:
                    self.check(pid, ppid, kill, parent_chain_oracle(pid, ppid, kill))
                    checks += 1
        self.assertEqual((trees, checks), (5914, 46233))

    def test_fifty_thousand_depth_width_and_unsorted_example(self):
        pid = list(range(1, 50001))
        chain = list(range(50000))
        self.check(pid, chain, 1, set(pid))
        self.check(pid, chain, 25000, set(range(25000, 50001)))
        self.check(pid, chain, 50000, {50000})
        star = [0] + [1] * 49999
        self.check(pid, star, 1, set(pid))
        self.check(pid, star, 50000, {50000})
        self.check([1, 3, 10, 5], [3, 0, 5, 3], 5, {5, 10})


if __name__ == '__main__':
    unittest.main()
