class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        previous = planted = 0
        for index, value in enumerate(flowerbed):
            following = flowerbed[index + 1] if index + 1 < len(flowerbed) else 0
            if value == previous == following == 0:
                planted += 1
                previous = 1
            else:
                previous = value
        return planted >= n
