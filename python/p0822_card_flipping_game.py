class Solution:
    def flipgame(self, fronts, backs):
        forbidden = {front for front,back in zip(fronts,backs) if front == back}
        answer = None
        for values in (fronts,backs):
            for value in values:
                if value not in forbidden and (answer is None or value < answer):
                    answer = value
        return 0 if answer is None else answer
