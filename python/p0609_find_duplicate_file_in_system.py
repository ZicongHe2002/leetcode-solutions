class Solution:
    def findDuplicate(self, paths):
        by_content = {}
        for info in paths:
            directory, *files = info.split(' ')
            for entry in files:
                opening = entry.index('(')
                name = entry[:opening]
                content = entry[opening + 1:-1]
                by_content.setdefault(content, []).append((directory, name))
        return [[directory + '/' + name for directory, name in group]
                for group in by_content.values() if len(group) > 1]
