class Solution:
    def simplifyPath(self, path):
        components = []
        for component in path.split('/'):
            if not component or component == '.':
                continue
            if component == '..':
                if components:
                    components.pop()
            else:
                components.append(component)
        return '/' + '/'.join(components)
