class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        x = []
        for i in range(1, n + 1):
            x.append(i)
        y = list(permutations(x))
        a = y[k - 1]
        return "".join(str(n) for n in a)