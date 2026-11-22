class Solution:
    def asteroidCollision(self, asteroids):
        survivors = []
        for asteroid in asteroids:
            while survivors and survivors[-1] > 0 and asteroid < 0:
                if survivors[-1] < -asteroid:
                    survivors.pop()
                    continue
                if survivors[-1] == -asteroid:
                    survivors.pop()
                break
            else:
                survivors.append(asteroid)
        return survivors
