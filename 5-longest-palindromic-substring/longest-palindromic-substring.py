class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)       # odd-length palindrome
            len2 = self.expandFromCenter(s, i, i + 1)   # even-length palindrome

            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expandFromCenter(self, s, left, right):
        # expand around the center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return the palindrome length
        return right - left - 1
