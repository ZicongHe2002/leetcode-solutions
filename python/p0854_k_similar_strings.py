from collections import deque


class Solution:
    def kSimilarity(self, s1, s2):
        if s1 == s2:
            return 0
        queue = deque([(s1,0)])
        seen = {s1}
        while queue:
            state,distance = queue.popleft()
            first = next(index for index in range(len(state)) if state[index] != s2[index])
            for second in range(first + 1,len(state)):
                if state[second] == s2[first] and state[second] != s2[second]:
                    letters = list(state)
                    letters[first],letters[second] = letters[second],letters[first]
                    following = ''.join(letters)
                    if following == s2:
                        return distance + 1
                    if following not in seen:
                        seen.add(following)
                        queue.append((following,distance + 1))
        return -1
