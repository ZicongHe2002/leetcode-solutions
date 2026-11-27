from collections import deque


class Solution:
    def catMouseGame(self, graph):
        size = len(graph)
        color = [[[0,0] for _ in range(size)] for _ in range(size)]
        degree = [[[len(graph[mouse]),sum(node != 0 for node in graph[cat])]
                   for cat in range(size)] for mouse in range(size)]
        queue = deque()
        for cat in range(1,size):
            for turn in (0,1):
                color[0][cat][turn] = 1
                queue.append((0,cat,turn))
        for node in range(1,size):
            for turn in (0,1):
                color[node][node][turn] = 2
                queue.append((node,node,turn))
        for mouse in range(size):
            for cat in range(1,size):
                for turn in (0,1):
                    if color[mouse][cat][turn] == 0 and degree[mouse][cat][turn] == 0:
                        color[mouse][cat][turn] = 2 if turn == 0 else 1
                        queue.append((mouse,cat,turn))
        while queue:
            mouse,cat,turn = queue.popleft()
            winner = color[mouse][cat][turn]
            if turn == 0:
                parents = ((mouse,previous,1) for previous in graph[cat] if previous != 0)
            else:
                parents = ((previous,cat,0) for previous in graph[mouse])
            for previous_mouse,previous_cat,previous_turn in parents:
                if color[previous_mouse][previous_cat][previous_turn]:
                    continue
                mover = 1 if previous_turn == 0 else 2
                if winner == mover:
                    color[previous_mouse][previous_cat][previous_turn] = winner
                    queue.append((previous_mouse,previous_cat,previous_turn))
                else:
                    degree[previous_mouse][previous_cat][previous_turn] -= 1
                    if degree[previous_mouse][previous_cat][previous_turn] == 0:
                        color[previous_mouse][previous_cat][previous_turn] = winner
                        queue.append((previous_mouse,previous_cat,previous_turn))
        return color[1][2][0]
