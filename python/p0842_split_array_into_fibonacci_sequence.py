class Solution:
    def splitIntoFibonacci(self, num):
        limit = 2**31 - 1
        size = len(num)
        for first_end in range(1,min(10,size - 2) + 1):
            if num[0] == '0' and first_end > 1:
                break
            first = int(num[:first_end])
            if first > limit:
                break
            for second_end in range(first_end + 1,min(first_end + 10,size - 1) + 1):
                if num[first_end] == '0' and second_end > first_end + 1:
                    break
                second = int(num[first_end:second_end])
                if second > limit:
                    break
                sequence = [first,second]
                position = second_end
                while position < size:
                    following = sequence[-2] + sequence[-1]
                    if following > limit:
                        break
                    text = str(following)
                    if not num.startswith(text,position):
                        break
                    sequence.append(following)
                    position += len(text)
                if position == size and len(sequence) >= 3:
                    return sequence
        return []
