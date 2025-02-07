class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        rev = " ".join(reversed(x))
        return rev