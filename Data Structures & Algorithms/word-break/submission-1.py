class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l, r = 0, 0
        while True:
            if s[l:r+1] in wordDict:
                print(s[l:r+1], l, r)
                if r + 1 >= len(s):
                    return True
                l = r + 1
            else:
                r += 1
            if r > len(s):
                return False