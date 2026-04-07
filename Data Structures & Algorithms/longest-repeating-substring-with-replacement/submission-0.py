class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        for r in range(0, len(s)):
            if s[l] != s[r]:
                if k > 0:
                    k -= 1
                    res += 1
            else:
                res += 1
        return res