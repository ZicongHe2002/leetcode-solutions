class Solution:
    def optimalDivision(self, nums):
        terms = list(map(str, nums))
        if len(terms) <= 2:
            return '/'.join(terms)
        return terms[0] + '/(' + '/'.join(terms[1:]) + ')'
