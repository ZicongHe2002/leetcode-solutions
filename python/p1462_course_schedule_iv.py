class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        reach = [[False] * numCourses for _ in range(numCourses)]
        for first, second in prerequisites:
            reach[first][second] = True
        for middle in range(numCourses):
            for first in range(numCourses):
                if reach[first][middle]:
                    for second in range(numCourses):
                        reach[first][second] |= reach[middle][second]
        return [reach[first][second] for first, second in queries]
