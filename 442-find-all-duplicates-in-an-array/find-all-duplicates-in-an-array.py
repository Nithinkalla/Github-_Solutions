class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = set()
        y = set()
        for i in nums:
            if i in x:
                y.add(i)
            else:
                x.add(i)
        return list(y)