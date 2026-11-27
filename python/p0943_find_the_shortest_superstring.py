class Solution:
    def shortestSuperstring(self, words):
        unique = list(dict.fromkeys(words))
        values = [word for index,word in enumerate(unique)
                  if not any(index != other and word in candidate for other,candidate in enumerate(unique))]
        size = len(values)
        if size == 0:
            return ''
        overlap = [[0] * size for _ in range(size)]
        for first in range(size):
            for second in range(size):
                if first == second:
                    continue
                for length in range(min(len(values[first]),len(values[second])),0,-1):
                    if values[first].endswith(values[second][:length]):
                        overlap[first][second] = length
                        break
        best = [[None] * size for _ in range(1 << size)]
        for index,word in enumerate(values):
            best[1 << index][index] = word
        for mask in range(1,1 << size):
            for last in range(size):
                current = best[mask][last]
                if current is None:
                    continue
                for following in range(size):
                    if mask & (1 << following):
                        continue
                    next_mask = mask | (1 << following)
                    candidate = current + values[following][overlap[last][following]:]
                    previous = best[next_mask][following]
                    if previous is None or len(candidate) < len(previous):
                        best[next_mask][following] = candidate
        return min(best[-1],key=len)
