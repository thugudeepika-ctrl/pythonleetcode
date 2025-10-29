class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Ignore leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for optional sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Convert digits to integer
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Step 4: Handle overflow before it happens
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

        