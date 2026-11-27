class Solution:
    def subarrayBitwiseORs(self, arr):
        ending = set()
        all_values = set()
        for value in arr:
            ending = {value} | {previous | value for previous in ending}
            all_values.update(ending)
        return len(all_values)
