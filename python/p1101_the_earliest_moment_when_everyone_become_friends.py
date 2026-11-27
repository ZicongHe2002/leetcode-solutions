class Solution:
    def earliestAcq(self, logs, n):
        parent = list(range(n))
        size = [1] * n
        groups = n

        def find(person):
            while person != parent[person]:
                parent[person] = parent[parent[person]]
                person = parent[person]
            return person

        for timestamp, first, second in sorted(logs):
            first, second = find(first), find(second)
            if first == second:
                continue
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]
            groups -= 1
            if groups == 1:
                return timestamp
        return -1
