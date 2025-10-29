class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Get the sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before it happens
            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev

        