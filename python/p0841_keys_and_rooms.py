class Solution:
    def canVisitAllRooms(self, rooms):
        seen = {0}
        pending = [0]
        while pending:
            room = pending.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    pending.append(key)
        return len(seen) == len(rooms)
