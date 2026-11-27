from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        counts = Counter()
        for entry in cpdomains:
            amount,domain = entry.split()
            amount = int(amount)
            labels = domain.split('.')
            for start in range(len(labels)):
                counts['.'.join(labels[start:])] += amount
        return [str(amount) + ' ' + domain for domain,amount in counts.items()]
