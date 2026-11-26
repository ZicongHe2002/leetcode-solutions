import unittest
from itertools import product

from python.p0433_minimum_genetic_mutation import Solution


def explicit_gene_graph(start, end, bank):
    if start == end:
        return 0
    if end not in bank:
        return -1
    nodes = sorted(set(bank) | {start})
    distance = [[1000] * len(nodes) for _ in nodes]
    for first, gene in enumerate(nodes):
        distance[first][first] = 0
        for second, other in enumerate(nodes):
            if sum(a != b for a, b in zip(gene, other)) == 1:
                distance[first][second] = 1
    for middle in range(len(nodes)):
        for first in range(len(nodes)):
            for second in range(len(nodes)):
                distance[first][second] = min(distance[first][second], distance[first][middle] + distance[middle][second])
    result = distance[nodes.index(start)][nodes.index(end)]
    return result if result < 1000 else -1


class GeneMutationTests(unittest.TestCase):
    def check(self, start, end, bank, expected=None):
        before = bank[:]
        if expected is None:
            expected = explicit_gene_graph(start, end, bank)
        result = Solution().minMutation(start, end, bank)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(bank, before)

    def test_all_small_banks_and_endpoint_pairs_against_explicit_graph(self):
        genes = [''.join(prefix) + 'A' * 5 for prefix in product('AC', repeat=3)]
        checks = 0
        for mask in range(1 << len(genes)):
            bank = [gene for index, gene in enumerate(genes) if mask >> index & 1]
            for start in genes:
                for end in genes:
                    self.check(start, end, bank)
                    checks += 1
        self.assertEqual(checks, 16384)

    def test_maximum_bank_all_eight_positions_decoys_empty_and_missing_end(self):
        bank = ['C' * count + 'A' * (8 - count) for count in range(1, 9)] + ['GGGGGGGG', 'TTTTTTTT']
        self.assertEqual(len(bank), 10)
        self.check('AAAAAAAA', 'CCCCCCCC', bank, 8)
        self.check('AAAAAAAA', 'CCCCCCCC', ['CCCCCCCC'], -1)
        self.check('AAAAAAAA', 'AAAAAAAA', [], 0)
        self.check('AAAAAAAA', 'AAAAAAAT', [], -1)
        self.check('AAAAAAAA', 'AAAAAAAT', ['AAAAAAAT'], 1)


if __name__ == '__main__':
    unittest.main()
