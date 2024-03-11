class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = dict(zip(heights,names))
        y = []
        heights.sort(reverse = True)
        for i in heights:
            y.append(x[i])
        return y