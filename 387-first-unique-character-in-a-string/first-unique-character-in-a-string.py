from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        a = []
        for k,v in x.items():
            if v == 1:
                a.append(k)
        if a:
            b = a[0]
            return s.index(b)
        else:
            return -1