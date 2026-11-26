class Solution:
    def fizzBuzz(self, n):
        answer = []
        for value in range(1, n + 1):
            text = ''
            if value % 3 == 0:
                text += 'Fizz'
            if value % 5 == 0:
                text += 'Buzz'
            answer.append(text or str(value))
        return answer
