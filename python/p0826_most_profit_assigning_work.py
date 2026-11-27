class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty,profit))
        index = best = answer = 0
        for ability in sorted(worker):
            while index < len(jobs) and jobs[index][0] <= ability:
                best = max(best,jobs[index][1])
                index += 1
            answer += best
        return answer
