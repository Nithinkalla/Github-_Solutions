class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxlen = 1
        maxstr = s[0]
        for i in range(len(s)):
            for j in range(i + 1,len(s)):
                if j - i + 1 > maxlen and s[i:j + 1] == s[i:j + 1][::-1]:
                    maxlen = j - i + 1
                    maxstr = s[i:j + 1]
        return maxstr