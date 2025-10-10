class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i + len(p)]) == x:
                res.append(i)
        return res