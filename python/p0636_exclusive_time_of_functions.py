class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        previous = 0
        for log in logs:
            identifier, event, timestamp = log.split(':')
            identifier, timestamp = int(identifier), int(timestamp)
            if event == 'start':
                if stack:
                    result[stack[-1]] += timestamp - previous
                stack.append(identifier)
                previous = timestamp
            else:
                result[stack.pop()] += timestamp - previous + 1
                previous = timestamp + 1
        return result
