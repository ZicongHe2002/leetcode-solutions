class Solution:
    def reconstructQueue(self, people):
        result = []
        for height, count in sorted(people, key=lambda person: (-person[0], person[1])):
            result.insert(count, [height, count])
        return result
