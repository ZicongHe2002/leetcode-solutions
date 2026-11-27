class Solution:
    def findItinerary(self, tickets):
        flights = {}
        for origin, destination in tickets:
            flights.setdefault(origin, []).append(destination)
        for destinations in flights.values():
            destinations.sort(reverse=True)
        stack, reversed_route = ['JFK'], []
        while stack:
            destinations = flights.get(stack[-1])
            if destinations:
                stack.append(destinations.pop())
            else:
                reversed_route.append(stack.pop())
        return reversed_route[::-1]
