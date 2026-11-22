import unittest

from python.p0997_find_the_town_judge import Solution


def direct_judge_predicates(n, trust):
    relations = {tuple(pair) for pair in trust}
    candidates = [person for person in range(1, n + 1)
                  if not any(source == person for source, _ in relations)
                  and all((other, person) in relations for other in range(1, n + 1) if other != person)]
    return candidates[0] if len(candidates) == 1 else -1


class TrustNetDegreeJudgeTests(unittest.TestCase):
    def check(self, n, trust, expected=None):
        before = [pair[:] for pair in trust]
        if expected is None:
            expected = direct_judge_predicates(n, trust)
        result = Solution().findJudge(n, trust)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(trust, before)

    def test_all_small_distinct_nonself_trust_relations(self):
        checks = 0
        for n in range(1, 5):
            possible = [(source, target) for source in range(1, n + 1)
                        for target in range(1, n + 1) if source != target]
            for mask in range(1 << len(possible)):
                self.check(n, [list(pair) for index, pair in enumerate(possible) if mask >> index & 1])
                checks += 1
        self.assertEqual(checks, 4165)

    def test_maximum_population_relationships_and_disqualifying_outedge(self):
        n = 1000
        trust = [[person, n] for person in range(1, n)]
        for source in range(1, n):
            for target in range(1, n):
                if source != target:
                    trust.append([source, target])
                    if len(trust) == 10000:
                        break
            if len(trust) == 10000:
                break
        self.assertEqual(len({tuple(pair) for pair in trust}), 10000)
        self.check(n, trust, n)
        self.check(n, [[person, n] for person in range(1, n)] + [[n, 1]], -1)
        self.check(n, [], -1)
        self.check(n, [[person, person % n + 1] for person in range(1, n + 1)], -1)
        self.check(1, [], 1)


if __name__ == '__main__':
    unittest.main()
