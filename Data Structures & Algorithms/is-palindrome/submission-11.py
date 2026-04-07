class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        chars = string.ascii_lowercase + string.digits
        s = "".join(s.lower().split(" "))
        finalS = ""
        for c in s:
            if c in chars:
                finalS += c
        return finalS[::-1] == finalS