from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        followers = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            followers[prerequisite].append(course)
            indegree[course] += 1
        pending = deque(course for course in range(numCourses) if indegree[course] == 0)
        result = []
        while pending:
            course = pending.popleft()
            result.append(course)
            for follower in followers[course]:
                indegree[follower] -= 1
                if indegree[follower] == 0:
                    pending.append(follower)
        return result if len(result) == numCourses else []
