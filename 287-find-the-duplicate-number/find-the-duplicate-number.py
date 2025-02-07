class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = Counter(nums)
        for k,v in x.items():
            if v >= 2:
                return k