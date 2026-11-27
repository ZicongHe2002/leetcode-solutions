class Solution:
    def corpFlightBookings(self, bookings, n):
        changes = [0] * (n + 1)
        for first, last, seats in bookings:
            changes[first - 1] += seats
            changes[last] -= seats
        answer = []
        booked = 0
        for flight in range(n):
            booked += changes[flight]
            answer.append(booked)
        return answer
