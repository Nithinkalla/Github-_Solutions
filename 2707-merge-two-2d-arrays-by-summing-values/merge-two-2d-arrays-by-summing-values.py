class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x = Counter()
        for id1,val in nums1:
            x[id1] += val
        for id1,val in nums2:
            x[id1] += val
        return sorted(x.items())