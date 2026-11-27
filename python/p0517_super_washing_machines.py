class Solution:
    def findMinMoves(self, machines):
        if not machines:
            return 0
        total = sum(machines)
        if total % len(machines):
            return -1
        average = total // len(machines)
        flow = answer = 0
        for load in machines:
            surplus = load - average
            flow += surplus
            answer = max(answer, abs(flow), surplus)
        return answer
