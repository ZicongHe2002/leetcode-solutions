import heapq


class Solution:
    def scheduleCourse(self, courses):
        selected = []
        elapsed = 0
        for duration, deadline in sorted(courses, key=lambda course: course[1]):
            heapq.heappush(selected, -duration)
            elapsed += duration
            if elapsed > deadline:
                elapsed += heapq.heappop(selected)
        return len(selected)
