from bisect import insort


class ExamRoom:
    def __init__(self, n):
        self.capacity = n
        self.occupied = []

    def seat(self):
        if not self.occupied:
            self.occupied.append(0)
            return 0
        chosen = 0
        distance = self.occupied[0]
        for left,right in zip(self.occupied,self.occupied[1:]):
            candidate_distance = (right - left) // 2
            if candidate_distance > distance:
                distance = candidate_distance
                chosen = left + candidate_distance
        if self.capacity - 1 - self.occupied[-1] > distance:
            chosen = self.capacity - 1
        insort(self.occupied,chosen)
        return chosen

    def leave(self, p):
        self.occupied.remove(p)
