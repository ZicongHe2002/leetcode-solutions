class Solution:
    def sortArray(self, nums):
        source = nums[:]
        size = len(source)
        buffer = [0] * size
        width = 1
        while width < size:
            for left in range(0,size,2 * width):
                middle = min(left + width,size)
                right = min(left + 2 * width,size)
                first,second = left,middle
                for destination in range(left,right):
                    if second >= right or first < middle and source[first] <= source[second]:
                        buffer[destination] = source[first]
                        first += 1
                    else:
                        buffer[destination] = source[second]
                        second += 1
            source,buffer = buffer,source
            width *= 2
        return source
