class Solution:
    def findCircleNum(self, isConnected):
        visited = [False] * len(isConnected)
        provinces = 0
        for start in range(len(isConnected)):
            if visited[start]:
                continue
            provinces += 1
            visited[start] = True
            pending = [start]
            while pending:
                city = pending.pop()
                for neighbor, connected in enumerate(isConnected[city]):
                    if connected and not visited[neighbor]:
                        visited[neighbor] = True
                        pending.append(neighbor)
        return provinces
