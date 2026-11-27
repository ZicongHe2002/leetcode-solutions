from collections import Counter


class Solution:
    def numRabbits(self, answers):
        return sum((count + answer) // (answer + 1) * (answer + 1)
                   for answer, count in Counter(answers).items())
