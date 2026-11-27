class Solution:
    def bagOfTokensScore(self, tokens, power):
        values = sorted(tokens)
        left,right = 0,len(values) - 1
        score = best = 0
        while left <= right:
            if power >= values[left]:
                power -= values[left]
                score += 1
                left += 1
                best = max(best,score)
            elif score > 0 and left < right:
                power += values[right]
                score -= 1
                right -= 1
            else:
                break
        return best
