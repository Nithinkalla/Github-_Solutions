class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x = []
        c = k
        i = len(num) - 1
        while i >= 0 or c > 0:
            if i >= 0:
                c += num[i]
                i -= 1
            x.append(c % 10)
            c //= 10
        return x[::-1]