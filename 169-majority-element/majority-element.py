from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = Counter(nums)
        y = x.values()
        z = max(y)
        res = [k for k,v in x.items() if v == z]
        for i in res:
            return i