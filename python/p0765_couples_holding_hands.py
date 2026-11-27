class Solution:
    def minSwapsCouples(self, row):
        seats = row[:]
        position = [0] * len(seats)
        for index, person in enumerate(seats):
            position[person] = index
        swaps = 0
        for index in range(0, len(seats), 2):
            partner = seats[index] ^ 1
            if seats[index + 1] != partner:
                other = seats[index + 1]
                location = position[partner]
                seats[index + 1], seats[location] = partner, other
                position[partner], position[other] = index + 1, location
                swaps += 1
        return swaps
