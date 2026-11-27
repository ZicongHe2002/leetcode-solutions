class Solution:
    def findMode(self, root):
        maximum = 0
        modes = []

        def scan(collect):
            nonlocal maximum
            current = root
            previous = None
            run = 0
            while current is not None:
                if current.left is not None:
                    predecessor = current.left
                    while predecessor.right is not None and predecessor.right is not current:
                        predecessor = predecessor.right
                    if predecessor.right is None:
                        predecessor.right = current
                        current = current.left
                        continue
                    predecessor.right = None
                value = current.val
                run = run + 1 if value == previous else 1
                if collect:
                    if run == maximum:
                        modes.append(value)
                else:
                    maximum = max(maximum, run)
                previous = value
                current = current.right

        scan(False)
        scan(True)
        return modes
