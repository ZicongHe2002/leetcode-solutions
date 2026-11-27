class Solution:
    def prisonAfterNDays(self, cells, n):
        state = tuple(cells)
        seen = {}
        history = []
        while n > 0 and state not in seen:
            seen[state] = len(history)
            history.append(state)
            state = (0,) + tuple(int(state[index - 1] == state[index + 1]) for index in range(1,7)) + (0,)
            n -= 1
        if n > 0:
            beginning = seen[state]
            period = len(history) - beginning
            state = history[beginning + n % period]
        return list(state)
