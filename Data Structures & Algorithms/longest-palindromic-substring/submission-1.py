class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        isPalindrome = lambda s1: s1 == s1[::-1]

        for l in range(len(s)):
            for r in range(l, len(s)):
                subStr = s[l:r+1]
                if isPalindrome(subStr) and len(subStr) > len(longest):
                    longest = subStr
        return longest