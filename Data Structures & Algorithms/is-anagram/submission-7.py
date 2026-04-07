class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(list(s), list(t).sort())
        return list(s).sort() == list(t).sort()