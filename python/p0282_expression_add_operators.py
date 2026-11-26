class Solution:
    def addOperators(self, num, target):
        answers = []

        def search(start, expression, total, last):
            if start == len(num):
                if total == target:
                    answers.append(expression)
                return
            for end in range(start + 1, len(num) + 1):
                if end > start + 1 and num[start] == '0':
                    break
                text = num[start:end]
                value = int(text)
                if start == 0:
                    search(end, text, value, value)
                else:
                    search(end, expression + '+' + text, total + value, value)
                    search(end, expression + '-' + text, total - value, -value)
                    product = last * value
                    search(end, expression + '*' + text, total - last + product, product)

        search(0, '', 0, 0)
        return answers
