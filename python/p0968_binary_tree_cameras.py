class Solution:
    def minCameraCover(self, root):
        states = {None:2}
        stack = [(root,False)]
        cameras = 0
        while stack:
            node,ready = stack.pop()
            if node is None:
                continue
            if not ready:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))
                continue
            left,right = states[node.left],states[node.right]
            if left == 0 or right == 0:
                cameras += 1
                states[node] = 1
            elif left == 1 or right == 1:
                states[node] = 2
            else:
                states[node] = 0
        return cameras + (states[root] == 0)
