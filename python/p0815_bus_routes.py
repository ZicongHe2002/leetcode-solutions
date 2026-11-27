from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        through = defaultdict(list)
        for route,stops in enumerate(routes):
            for stop in stops:
                through[stop].append(route)
        queue = deque([(source,0)])
        seen_stops = {source}
        seen_routes = set()
        while queue:
            stop,buses = queue.popleft()
            for route in through[stop]:
                if route in seen_routes:
                    continue
                seen_routes.add(route)
                for destination in routes[route]:
                    if destination == target:
                        return buses + 1
                    if destination not in seen_stops:
                        seen_stops.add(destination)
                        queue.append((destination,buses + 1))
        return -1
