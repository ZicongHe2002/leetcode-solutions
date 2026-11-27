class Solution:
    def distributeCandies(self, candies, num_people):
        answer = [0] * num_people
        gift = 1
        while candies:
            amount = min(gift, candies)
            answer[(gift - 1) % num_people] += amount
            candies -= amount
            gift += 1
        return answer
