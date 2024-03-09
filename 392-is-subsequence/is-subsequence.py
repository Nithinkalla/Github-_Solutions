class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        for i in t:
            if x >= len(s):
                break
            if s[x] == i:
                x += 1
        return x == len(s) 






