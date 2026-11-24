from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        dependents = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            dependents[prerequisite].append(course)
            indegree[course] += 1
        available = deque(course for course in range(numCourses) if indegree[course] == 0)
        finished = 0
        while available:
            prerequisite = available.popleft()
            finished += 1
            for course in dependents[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    available.append(course)
        return finished == numCourses
