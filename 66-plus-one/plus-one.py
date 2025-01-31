class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(map(str,digits))
        y = int(x) + 1
        z = str(y)
        a = [int(i) for i in z]
        return a