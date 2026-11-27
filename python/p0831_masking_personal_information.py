class Solution:
    def maskPII(self, s):
        if '@' in s:
            name,domain = s.lower().split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        digits = ''.join(char for char in s if char.isdigit())
        local = '***-***-' + digits[-4:]
        country_length = len(digits) - 10
        if country_length:
            return '+' + '*' * country_length + '-' + local
        return local
