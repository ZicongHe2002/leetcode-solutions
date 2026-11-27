from heapq import heappush, heapreplace


class Solution:
    def highFive(self, items):
        scores = {}
        for student, score in items:
            best = scores.setdefault(student, [])
            if len(best) < 5:
                heappush(best, score)
            elif score > best[0]:
                heapreplace(best, score)
        return [[student, sum(scores[student]) // 5] for student in sorted(scores)]
