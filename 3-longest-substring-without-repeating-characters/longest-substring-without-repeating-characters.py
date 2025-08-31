class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlength = 0
        seen = {}
        for right,char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            maxlength = max(maxlength,right-left + 1)
        return maxlength

