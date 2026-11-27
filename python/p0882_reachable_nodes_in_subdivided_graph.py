import heapq


class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        neighbors = [[] for _ in range(n)]
        for first,second,subdivisions in edges:
            weight = subdivisions + 1
            neighbors[first].append((second,weight))
            neighbors[second].append((first,weight))
        distance = [float('inf')] * n
        distance[0] = 0
        queue = [(0,0)]
        while queue:
            spent,node = heapq.heappop(queue)
            if spent != distance[node]:
                continue
            for following,weight in neighbors[node]:
                candidate = spent + weight
                if candidate <= maxMoves and candidate < distance[following]:
                    distance[following] = candidate
                    heapq.heappush(queue,(candidate,following))
        answer = sum(value <= maxMoves for value in distance)
        for first,second,subdivisions in edges:
            from_first = max(0,maxMoves - distance[first])
            from_second = max(0,maxMoves - distance[second])
            answer += min(subdivisions,from_first + from_second)
        return answer
