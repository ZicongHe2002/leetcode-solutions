class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        secret_left = [0] * 10
        guess_left = [0] * 10
        for actual, proposed in zip(secret, guess):
            if actual == proposed:
                bulls += 1
            else:
                secret_left[ord(actual) - ord('0')] += 1
                guess_left[ord(proposed) - ord('0')] += 1
        cows = sum(min(first, second) for first, second in zip(secret_left, guess_left))
        return f'{bulls}A{cows}B'
