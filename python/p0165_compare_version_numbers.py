class Solution:
    def compareVersion(self, version1, version2):
        first, second = version1.split('.'), version2.split('.')
        for index in range(max(len(first), len(second))):
            left = int(first[index]) if index < len(first) else 0
            right = int(second[index]) if index < len(second) else 0
            if left != right:
                return 1 if left > right else -1
        return 0
