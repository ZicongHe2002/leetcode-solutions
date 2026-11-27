class Solution:
    def licenseKeyFormatting(self, s, k):
        cleaned = s.replace('-', '').upper()
        if not cleaned:
            return ''
        first = len(cleaned) % k or k
        groups = [cleaned[:first]]
        for start in range(first, len(cleaned), k):
            groups.append(cleaned[start:start + k])
        return '-'.join(groups)
