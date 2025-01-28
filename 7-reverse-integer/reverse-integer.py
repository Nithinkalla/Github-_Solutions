class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        z = list(y)
        jnstr = "".join(z)
        rev = jnstr[::-1]
        if x < 0:
            rev = "-" + rev[:-1]
        if int(rev) > 2**31 - 1 or int(rev) < -2**31:
            return 0
        return int(rev)