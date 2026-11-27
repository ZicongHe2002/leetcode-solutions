from bisect import bisect_right


class TopVotedCandidate:
    def __init__(self, persons, times):
        self.times = times[:]
        self.leaders = []
        counts = {}
        leader = None
        maximum = 0
        for person in persons:
            counts[person] = counts.get(person,0) + 1
            if counts[person] >= maximum:
                maximum = counts[person]
                leader = person
            self.leaders.append(leader)

    def q(self, t):
        return self.leaders[bisect_right(self.times,t) - 1]
