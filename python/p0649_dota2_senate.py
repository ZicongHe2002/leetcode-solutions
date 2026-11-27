from collections import deque


class Solution:
    def predictPartyVictory(self, senate):
        size = len(senate)
        radiant = deque(index for index, party in enumerate(senate) if party == 'R')
        dire = deque(index for index, party in enumerate(senate) if party == 'D')
        while radiant and dire:
            first_r, first_d = radiant.popleft(), dire.popleft()
            if first_r < first_d:
                radiant.append(first_r + size)
            else:
                dire.append(first_d + size)
        return 'Radiant' if radiant else 'Dire'
