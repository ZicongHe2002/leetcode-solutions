class Solution:
    def ipToCIDR(self, ip, n):
        start = 0
        for part in ip.split('.'):
            start = (start << 8) | int(part)
        result = []
        while n:
            alignment = start & -start or 1 << 32
            size = min(alignment, 1 << (n.bit_length() - 1))
            address = '.'.join(str((start >> shift) & 255) for shift in (24, 16, 8, 0))
            result.append(address + '/' + str(33 - size.bit_length()))
            start += size
            n -= size
        return result
