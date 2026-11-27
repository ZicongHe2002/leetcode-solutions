class Solution:
    def findRelativeRanks(self, score):
        order = sorted(range(len(score)), key=score.__getitem__, reverse=True)
        result = [''] * len(score)
        medals = ('Gold Medal', 'Silver Medal', 'Bronze Medal')
        for rank, index in enumerate(order, 1):
            result[index] = medals[rank - 1] if rank <= 3 else str(rank)
        return result
