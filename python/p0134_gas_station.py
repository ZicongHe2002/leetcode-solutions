class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0
        for index, (supply, expense) in enumerate(zip(gas, cost)):
            gain = supply - expense
            total += gain
            tank += gain
            if tank < 0:
                start = index + 1
                tank = 0
        return start if total >= 0 else -1
