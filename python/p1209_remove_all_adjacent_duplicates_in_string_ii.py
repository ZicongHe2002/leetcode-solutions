class Solution:
    def removeDuplicates(self, s, k):
        runs = []
        for letter in s:
            if runs and runs[-1][0] == letter:
                runs[-1][1] += 1
            else:
                runs.append([letter, 1])
            if runs[-1][1] == k:
                runs.pop()
        return ''.join(letter * count for letter, count in runs)
