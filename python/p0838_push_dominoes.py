class Solution:
    def pushDominoes(self, dominoes):
        size = len(dominoes)
        forces = [0] * size
        force = 0
        for index,char in enumerate(dominoes):
            if char == 'R':
                force = size
            elif char == 'L':
                force = 0
            else:
                force = max(0,force - 1)
            forces[index] += force
        force = 0
        for index in range(size - 1,-1,-1):
            char = dominoes[index]
            if char == 'L':
                force = size
            elif char == 'R':
                force = 0
            else:
                force = max(0,force - 1)
            forces[index] -= force
        return ''.join('R' if value > 0 else 'L' if value < 0 else '.' for value in forces)
