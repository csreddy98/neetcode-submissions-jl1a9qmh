class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().split(" "))
        finalS = []
        for c in s:
            if c.isalnum():
                finalS.append(c)
        finalS = "".join(finalS)
        return finalS[::-1] == finalS