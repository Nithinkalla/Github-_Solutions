class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = k
        i = len(num) - 1

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]  # Add current digit
                i -= 1
            res.append(carry % 10)  # Extract last digit
            carry //= 10  # Carry for next digit

        return res[::-1]  # Reverse to get the correct order
