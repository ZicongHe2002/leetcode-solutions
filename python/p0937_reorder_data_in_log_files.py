class Solution:
    def reorderLogFiles(self, logs):
        letters = []
        digits = []
        for log in logs:
            identifier,content = log.split(' ',1)
            if content[0].isdigit():
                digits.append(log)
            else:
                letters.append((content,identifier,log))
        letters.sort(key=lambda item:(item[0],item[1]))
        return [item[2] for item in letters] + digits
