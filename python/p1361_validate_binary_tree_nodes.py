class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        indegree = [0] * n
        for children in (leftChild, rightChild):
            for child in children:
                if child != -1:
                    indegree[child] += 1
                    if indegree[child] > 1:
                        return False
        roots = [node for node in range(n) if indegree[node] == 0]
        if len(roots) != 1:
            return False
        stack, seen = [roots[0]], set()
        while stack:
            node = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    stack.append(child)
        return len(seen) == n
