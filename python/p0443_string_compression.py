class Solution:
    def compress(self, chars):
        read = write = 0
        while read < len(chars):
            end = read + 1
            while end < len(chars) and chars[end] == chars[read]:
                end += 1
            count = end - read
            chars[write] = chars[read]
            write += 1
            if count > 1:
                divisor = 1
                while divisor * 10 <= count:
                    divisor *= 10
                while divisor:
                    chars[write] = chr(ord('0') + count // divisor)
                    write += 1
                    count %= divisor
                    divisor //= 10
            read = end
        return write
