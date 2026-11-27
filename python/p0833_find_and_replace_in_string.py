class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        replacements = {}
        for index,source,target in zip(indices,sources,targets):
            if s.startswith(source,index):
                replacements[index] = source,target
        result = []
        index = 0
        while index < len(s):
            if index in replacements:
                source,target = replacements[index]
                result.append(target)
                index += len(source)
            else:
                result.append(s[index])
                index += 1
        return ''.join(result)
