class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        charset = set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[i])
            maxlen = max(maxlen,i - left + 1)
        return maxlen
