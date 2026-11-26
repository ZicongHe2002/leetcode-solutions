class Solution:
    def validIPAddress(self, queryIP):
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return 'Neither'
            for part in parts:
                if not 1 <= len(part) <= 3 or any(char < '0' or char > '9' for char in part):
                    return 'Neither'
                if len(part) > 1 and part[0] == '0':
                    return 'Neither'
                if int(part) > 255:
                    return 'Neither'
            return 'IPv4'
        parts = queryIP.split(':')
        if len(parts) == 8 and all(1 <= len(part) <= 4 and
                                   all(char in '0123456789abcdefABCDEF' for char in part)
                                   for part in parts):
            return 'IPv6'
        return 'Neither'
