class _DisjointSet:
    def __init__(self, count):
        self.parent = list(range(count))
        self.size = [1] * count

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first, second):
        first, second = self.find(first), self.find(second)
        if first == second:
            return False
        if self.size[first] < self.size[second]:
            first, second = second, first
        self.parent[second] = first
        self.size[first] += self.size[second]
        return True



class Solution:
    def accountsMerge(self, accounts):
        groups = _DisjointSet(len(accounts))
        owner = {}
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in owner:
                    groups.union(index, owner[email])
                else:
                    owner[email] = index
        emails_by_root = {}
        for email, index in owner.items():
            root = groups.find(index)
            emails_by_root.setdefault(root, []).append(email)
        return [[accounts[root][0]] + sorted(emails)
                for root, emails in emails_by_root.items()]
