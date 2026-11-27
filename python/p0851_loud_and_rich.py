from collections import deque


class Solution:
    def loudAndRich(self, richer, quiet):
        size = len(quiet)
        poorer = [[] for _ in range(size)]
        indegree = [0] * size
        for rich,poor in richer:
            poorer[rich].append(poor)
            indegree[poor] += 1
        answer = list(range(size))
        queue = deque(person for person in range(size) if indegree[person] == 0)
        while queue:
            person = queue.popleft()
            for following in poorer[person]:
                if quiet[answer[person]] < quiet[answer[following]]:
                    answer[following] = answer[person]
                indegree[following] -= 1
                if indegree[following] == 0:
                    queue.append(following)
        return answer
