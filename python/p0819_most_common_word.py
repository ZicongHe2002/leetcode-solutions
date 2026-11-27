import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        forbidden = set(banned)
        counts = Counter(word for word in re.findall(r'[a-z]+',paragraph.lower()) if word not in forbidden)
        return max(counts,key=counts.get)
