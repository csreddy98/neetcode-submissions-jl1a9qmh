class Solution:
    def countSubstrings(self, s: str) -> int:
        isPalindrome = lambda s1: s1 == s1[::-1]
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    res += 1
        return res