class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for i in strs:
            y = "".join(sorted(i))
            x[y].append(i)
        return list(x.values())