from itertools import combinations, product
import unittest

from python.p0721_accounts_merge import Solution


def email_graph_components(accounts):
    adjacency, names = {}, {}
    for name, *emails in accounts:
        for email in emails:
            names[email] = name
            adjacency.setdefault(email, set()).update(emails)
    seen, result = set(), []
    for start in adjacency:
        if start in seen:
            continue
        seen.add(start)
        pending, group = [start], []
        while pending:
            email = pending.pop()
            group.append(email)
            for neighbor in adjacency[email]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        result.append([names[start]] + sorted(group))
    return result


class AccountEmailComponentsTests(unittest.TestCase):
    def check(self, accounts):
        before = [row[:] for row in accounts]
        expected = email_graph_components(accounts)
        result = Solution().accountsMerge(accounts)
        self.assertIs(type(result), list)
        for row in result:
            self.assertIs(type(row), list)
            self.assertEqual(row[1:], sorted(set(row[1:])))
        self.assertEqual(sorted(map(tuple, result)), sorted(map(tuple, expected)))
        self.assertEqual(accounts, before)

    def test_all_small_same_name_email_subset_sequences(self):
        emails = ('a@x.com', 'b@x.com', 'c@x.com')
        subsets = [subset for size in range(1, 4) for subset in combinations(emails, size)]
        checks = 0
        for count in range(1, 5):
            for group in product(subsets, repeat=count):
                self.check([['Alex', *subset] for subset in group])
                checks += 1
        self.assertEqual(checks, 2800)

    def test_maximum_accounts_row_length_transitivity_and_separate_names(self):
        accounts = [['A' * 30, f'bridge{index}@x.com', f'bridge{index + 1}@x.com']
                    + [f'p{index}_{offset}@x.com' for offset in range(7)]
                    for index in range(1000)]
        self.assertTrue(all(len(account) == 10 for account in accounts))
        self.check(accounts)
        self.check([['Alex'] + [f'e{index}_{offset}@x.com' for offset in range(9)]
                    for index in range(1000)])
        self.check([['John', 'a@x.com'], ['Mary', 'b@x.com'], ['John', 'c@x.com']])
        self.check([['Alex', 'a@x.com', 'a@x.com'], ['Alex', 'a@x.com', 'b@x.com']])


if __name__ == '__main__':
    unittest.main()
