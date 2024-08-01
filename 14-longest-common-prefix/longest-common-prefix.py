class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        fst = strs[0]
        lst = strs[-1]
        for i in range(min(len(fst),len(lst))):
            if (fst[i] != lst[i]):
                return ans
            ans += fst[i]
        return ans