class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        uniqChars = set()
        l, r = 0, 1
        uniqChars.add(s[l])
        res = 1
        while r < len(s):
            if s[r] not in uniqChars:
                uniqChars.add(s[r])
            else:
                uniqChars = set()
                l += 1
                uniqChars.add(s[l])
            res = max(res, len(uniqChars))
            r += 1
        return res