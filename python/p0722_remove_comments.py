class Solution:
    def removeComments(self, source):
        result, pending = [], []
        inside_block = False
        for line in source:
            index = 0
            while index < len(line):
                pair = line[index:index + 2]
                if inside_block:
                    if pair == '*/':
                        inside_block = False
                        index += 2
                    else:
                        index += 1
                elif pair == '//':
                    break
                elif pair == '/*':
                    inside_block = True
                    index += 2
                else:
                    pending.append(line[index])
                    index += 1
            if not inside_block and pending:
                result.append(''.join(pending))
                pending.clear()
        return result
